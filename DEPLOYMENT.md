# Deployment — quick reference

How the FlexiVision One docs site gets deployed.&#x20;

## Architecture in one paragraph

Pushes to `main` trigger GitHub Actions. Media (`build/_shared/`,\
`build/_assets/`, `build/Offline manual.zip`) syncs to an **AWS S3** bucket\
fronted by **CloudFront**. HTML is baked into a tiny nginx Docker image\
pushed to **GHCR** (`ghcr.io/<owner>/flexivision-docs:latest`). A webhook\
notifies the Makai Labs deployment server to pull the new image and\
restart. Live site: `docs.flexibowl.com`.

## Everyday workflow

- ARS runs `build_manual.bat`, commits, pushes to `main`.
- Site updates within \~1–2 minutes. Nothing else to do.

## Where things live

| Thing                                 | Location                                             |
| ------------------------------------- | ---------------------------------------------------- |
| Source + HTML output                  | This repo                                            |
| Build pipeline                        | `.github/workflows/deploy.yml`                       |
| Size guard (blocks big non-LFS files) | `.github/workflows/size-check.yml`                   |
| Docker image                          | `ghcr.io/<owner>/flexivision-docs`                   |
| Media & big files                     | AWS S3 bucket `flexivision-docs` (eu-south-1, Milan) |
| CDN in front of S3                    | AWS CloudFront distribution (URL in `CDN_BASE_URL` secret) |
| Runtime                               | Makai Labs deployment server                         |
| AWS + deploy credentials              | GitHub → Settings → Secrets (7 entries)              |

## Check deploy status

- **Currently deploying?** Repo → Actions tab. Green = done.
- **Deploy failed?** Click the red run, read the failed step.
- **Site stale?** Confirm the latest run is green in the Actions tab. If\
  it is but the site still shows old content after a few minutes, the\
  deployment server didn't pick up the new image — ping Makai Labs.
- **Media missing?** Check S3 bucket Objects tab for the file. If absent,\
  re-run the sync job manually from Actions.
- **Old media still showing?** CloudFront cache. Wait for TTL to expire,\
  or trigger an invalidation manually (AWS console → CloudFront →\
  distribution → Invalidations → `Create invalidation` → path `/*`).

## Common actions

### Rollback

1. Quick: revert the bad commit on `main`, push. CI re-deploys.
2. Faster: ask Makai Labs to swap the deployed image tag back to a\
   previous commit SHA. Every workflow run pushes both `:latest` and\
   `:<commit-sha>` to GHCR, so any past green commit is still pullable.

### Rotate AWS credentials

AWS IAM → Users → `github-actions-flexivision` → Security credentials →\
deactivate the old access key, create a new one → update\
`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` in GitHub Secrets.

### Extend the list of files that go to LFS

Edit `.gitattributes`, add the pattern, commit. New files follow the rule;\
old files stay where they are.

### Adding new downloads (zips, large PDFs, archives, etc.)

Drop the file under `build/_shared/` (a subdirectory like\
`build/_shared/downloads/` is fine) and link to it from your HTML with\
a normal relative path:

```html
<a href="../../_shared/downloads/MyManual_v2.zip">Download</a>
```

Commit and push as usual — that's it. CI takes care of the rest:

- the file is uploaded to the CDN (not into the docs site image), so it\
  stays fast even when it's very large;
- the link in your HTML is rewritten to point at the CDN automatically.

**Don't** drop new big files at the root of `build/` — those bloat the\
docs site image and bypass the CDN.

#### Special case: `build/Offline manual.zip`

This one archive lives at the root of `build/` because\
`build_manual.bat` writes it there, and the "Download offline manual"\
button inside the docs is built by JavaScript at page-load time against\
the docs domain. ARS doesn't have to do anything different — `git push`\
behaves the same. Behind the scenes, CI still uploads the archive to\
the CDN, and the deployment server has a hard-coded 302-redirect from\
`/Offline%20manual.zip` to the CDN, so the download streams from\
CloudFront like everything else.

If `build_manual.bat` is ever changed to rename or relocate this\
archive, ping Makai Labs so the redirect can be updated.

### Move to a different CDN URL or bucket

Update the `CDN_BASE_URL`, `S3_BUCKET_NAME`, and/or\
`CLOUDFRONT_DISTRIBUTION_ID` secret. Next push rewrites HTML URLs to the\
new target and syncs there.

### Force a fresh CDN cache

Manual invalidation in CloudFront, path `/*`. First 1000 invalidation\
paths/month are free; `/*` counts as one path.

## Known limits

- AWS S3 storage (Milan / eu-south-1): \~$0.0245/GB/month.
- CloudFront egress: \~$0.085/GB out (Europe/US). Expect \~$1–5/month for\
  a typical docs site.
- CloudFront invalidations: 1000 paths/month free, then $0.005/path.
- GitHub LFS: free up to 1 GB storage + 1 GB/month bandwidth. Buy a\
  $5/month pack if exceeded.
- Single file over 100 MB must be LFS-tracked or GitHub rejects the push.
- Size-check workflow blocks non-LFS files > 10 MB.

## If everything is on fire

- Ask Makai Labs to pause auto-deploy on the deployment server so a\
  broken push doesn't keep propagating while you investigate.
- Emergency fallback to GitHub Pages: restore\
  `.github/workflows/pages.yml` from git history (it was deleted when\
  the current deploy stack was set up). Once that workflow runs, the\
  site serves from `<owner>.github.io/<repo>` within \~2 minutes.

## Who to contact

- Repo + deploy: Makai Labs
- AWS account / CloudFront: Makai Labs
- ARS edits content only — he should not need to touch this file.


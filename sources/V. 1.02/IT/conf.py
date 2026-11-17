from pathlib import Path

exec((Path(__file__).resolve().parents[2] / "_shared" / "conf_common.py").read_text(encoding="utf-8"), globals())
html_extra_path = ['_shared/media/images', '_shared/media/videos']
html_js_files = ['custom.js']

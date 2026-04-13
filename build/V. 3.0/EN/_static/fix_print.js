window.onbeforeprint = () => {
    document.querySelectorAll('details.sd-dropdown').forEach((dropdown) => {
        dropdown.setAttribute('open', '');
    });
};

document.addEventListener('DOMContentLoaded', () => {
    const manifest = window.FV_VERSIONING;
    if (!manifest) {
        return;
    }

    const versions = Array.isArray(manifest.versions) ? manifest.versions : [];
    const languagesByVersion = manifest.languagesByVersion || {};
    const defaultLanguageByVersion = manifest.defaultLanguageByVersion || {};

    const pathSegments = window.location.pathname.split('/').filter(Boolean);
    const versionIndex = pathSegments.findIndex((segment) => versions.includes(decodeURIComponent(segment)));

    if (versionIndex === -1) {
        return;
    }

    const currentVersion = decodeURIComponent(pathSegments[versionIndex]);
    const currentLanguages = languagesByVersion[currentVersion] || [];
    const languageIndex = pathSegments.findIndex(
        (segment, index) => index > versionIndex && currentLanguages.includes(decodeURIComponent(segment))
    );

    if (languageIndex === -1) {
        return;
    }

    const currentLanguage = decodeURIComponent(pathSegments[languageIndex]);
    const baseSegments = pathSegments.slice(0, versionIndex);

    const bar = document.createElement('div');
    bar.className = 'fixed-bar';
    bar.setAttribute('role', 'region');
    bar.setAttribute('aria-label', 'Version and language selector');

    const makeDropdown = (label, values, current) => {
        const dropdown = document.createElement('div');
        dropdown.className = 'dropdown';

        const toggle = document.createElement('div');
        toggle.className = 'dropdown-toggle';
        toggle.tabIndex = 0;
        toggle.setAttribute('aria-haspopup', 'listbox');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.innerHTML = `<span class="fa ${label === 'Version' ? 'fa-book' : 'fa-globe'}" aria-hidden="true"></span>${label}: <span class="current-value">${current}</span><span class="fa caret-icon fa-caret-down" aria-hidden="true"></span>`;

        const menu = document.createElement('div');
        menu.className = 'dropdown-menu';
        menu.setAttribute('role', 'listbox');

        values.forEach((value) => {
            const link = document.createElement('a');
            link.href = '#';
            link.setAttribute('role', 'option');
            link.textContent = value;
            menu.appendChild(link);
        });

        dropdown.append(toggle, menu);
        return { dropdown, toggle, menu };
    };

    const versionDropdown = makeDropdown('Version', versions, currentVersion);
    const languageDropdown = makeDropdown('Language', currentLanguages, currentLanguage);
    bar.append(versionDropdown.dropdown, languageDropdown.dropdown);
    document.body.appendChild(bar);

    const dropdowns = [versionDropdown, languageDropdown];

    const closeAll = () => {
        dropdowns.forEach(({ toggle, menu }) => {
            menu.classList.remove('show');
            toggle.setAttribute('aria-expanded', 'false');
            const caret = toggle.querySelector('.caret-icon');
            if (caret) {
                caret.classList.remove('fa-caret-up');
                caret.classList.add('fa-caret-down');
            }
        });
    };

    const goTo = (version, language) => {
        const nextSegments = [...baseSegments, encodeURIComponent(version), encodeURIComponent(language), 'index.html'];
        window.location.pathname = `/${nextSegments.join('/')}`;
    };

    dropdowns.forEach(({ toggle, menu }, index) => {
        toggle.addEventListener('click', () => {
            const isOpen = toggle.getAttribute('aria-expanded') === 'true';
            closeAll();
            if (!isOpen) {
                menu.classList.add('show');
                toggle.setAttribute('aria-expanded', 'true');
                const caret = toggle.querySelector('.caret-icon');
                if (caret) {
                    caret.classList.remove('fa-caret-down');
                    caret.classList.add('fa-caret-up');
                }
            }
        });

        toggle.addEventListener('keydown', (event) => {
            if (event.key === 'Enter' || event.key === ' ') {
                event.preventDefault();
                toggle.click();
            }
        });

        menu.addEventListener('click', (event) => {
            const target = event.target;
            if (!(target instanceof HTMLAnchorElement)) {
                return;
            }

            event.preventDefault();
            const selected = target.textContent?.trim();
            if (!selected) {
                return;
            }

            if (index === 0) {
                const nextLanguage = defaultLanguageByVersion[selected] || (languagesByVersion[selected] || [])[0];
                if (nextLanguage) {
                    goTo(selected, nextLanguage);
                }
                return;
            }

            goTo(currentVersion, selected);
        });
    });

    document.addEventListener('click', (event) => {
        if (!bar.contains(event.target)) {
            closeAll();
        }
    });
});

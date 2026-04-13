# Configuration file shared by all Sphinx manuals.
#
# Each version/language `conf.py` loads this file so shared settings stay in
# one place and static assets can live under `sources/_shared/static`.

# -- Project information -----------------------------------------------------

project = "FlexiVision One"
author = "ARS Automation"
copyright = "2026, Ars Automation"
release = "1.0"

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinxcontrib.video",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_book_theme"
html_static_path = ["../../_shared/static"]
html_title = "FlexiVision One Manual"

html_css_files = [
    "custom.css",
]

html_js_files = [
    "versioning-data.js",
    "fix_print.js",
]

html_logo = "../../_shared/media/images/logo.png"

html_context = {
    "default_mode": "light",
}

html_theme_options = {
    "logo": {
        "image_light": "../../_shared/media/images/logo.png",
        "image_dark": "../../_shared/media/images/logo_dark.png",
    },
    "show_navbar_depth": 1,
    "show_prev_next": True,
}

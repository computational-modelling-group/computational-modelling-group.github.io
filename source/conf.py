# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Computational Modelling Group'
copyright = '2008-today, Hans Fangohr and others, Computational Modelling Group, University of Southampton'
author = 'Computational Modelling Group'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.githubpages',  # creates .nojekyll file in HTML directory
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "CMG"
html_theme = 'pydata_sphinx_theme'
# html_logo = '_static/cmg-logo.png'
html_static_path = ['_static']
html_theme_options = {
    "icon_links": [
        {
            "name": "Home page",
            "url": "https://cmg.soton.ac.uk",
            "icon": "fab fa-github-square",
        },
    ],
    "show_prev_next": False,
    "footer_end": False,  # do not show "pydata theme"
    'nosidebar': True,  # hide menu on the right as we haven't got enough subsections
    "secondary_sidebar_items": [],  # default is ["page-toc", "edit-this-page", "sourcelink"],


}


html_show_sphinx = False

linkcheck_ignore = ["about.html"]  # is only created after sphinx runs

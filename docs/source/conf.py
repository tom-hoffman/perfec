# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PERFEC System'
copyright = '2026, Tom Hoffman and E-Cubed students'
author = 'Tom Hoffman and E-Cubed students'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx_design']

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
	'.rst': 'restructuredtext',
	'.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'shibuya'
html_static_path = ['_static']
html_logo = "_static/logo.png"
html_theme_options = {
	"accent_color": "red",
}

# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'Minima'
copyright = '2026, Gabriel'
author = 'Gabriel'

# -- General configuration ---------------------------------------------------

extensions = [
    'myst_parser',
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- MyST Parser configuration -----------------------------------------------

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

import os

# Obter o idioma do ambiente do Read the Docs, padrão é 'en'
language = os.environ.get('READTHEDOCS_LANGUAGE', 'en')

# O documento principal da toctree.
if language in ['pt', 'pt-br', 'br']:
    master_doc = 'br/index'
else:
    master_doc = 'en/index'

# locale_dirs = ['locale/']   # Opcional se usar o gettext do Sphinx no futuro

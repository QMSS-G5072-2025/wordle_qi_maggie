# Add these lines at the TOP of the file (after the copyright line)
import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

# Find the extensions list and change it to:
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
]

# Find the html_theme line and change it to:
html_theme = 'sphinx_rtd_theme'

# Add these lines at the bottom of the file:
# Napoleon settings for Google/Numpy style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True

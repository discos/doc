# -*- coding: utf-8 -*-

import sys, os, time

# General configuration
# ---------------------
sys.path.append(os.path.abspath('ext'))

extensions = [
    'discos',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
]
mathjax_path = 'http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'


# Add any paths that contain templates here, relative to this directory.
templates_path = ['theme/templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General substitutions.
project = 'DISCOS Control Software'
copyright = '2006-%s, DISCOS Control Software Team' % time.strftime('%Y')

# We should get this information from somewhere in the sources
version = '0.4'
# The full version, including alpha/beta/rc tags.
release = '0.4'

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Require Sphinx 1.2 for build.
needs_sphinx = '1.2'


# Options for HTML output
# -----------------------

# Use the custom shinx_rtd_theme (readthedocs.org)
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = ['theme', sphinx_rtd_theme.get_html_theme_path()]

# Short title used e.g. for <title> HTML tags.
html_short_title = 'DISCOS documentation'

# Path to find HTML templates.
templates_path = ['theme/templates']
# Additional static files.
html_static_path = ['theme/static/']

# Custom sidebar templates, filenames relative to this file.
#html_sidebars = {}

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Output file base name for HTML help builder.
htmlhelp_basename = 'nuraghe'

# Split the index
# html_split_index = False


# Options for LaTeX output
# ------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = 'a4'

# The font size ('10pt', '11pt' or '12pt').
latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
latex_documents = [
  ('index', 
   'nuraghe-doc.tex', 
   u'DISCOS Documentation', 
   u'DISCOS CS team', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

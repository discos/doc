import sys, os, time

sys.path.append(os.path.abspath('ext'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DISCOS Control Software'
copyright = '2006-%s, DISCOS Control Software Team' % time.strftime('%Y')
version = '0.6'
release = '0.6'

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    'discos',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
]

templates_path = ['theme/templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = '.rst'
root_doc = 'index'

mathjax_path = 'http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme_path = ['theme']
html_theme = 'sphinx_rtd_theme'
html_static_path = ['theme/static/']

# Short title used e.g. for <title> HTML tags.
html_short_title = 'DISCOS documentation'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'discos.DISCOSStyle'

# Custom sidebar templates, filenames relative to this file.
#html_sidebars = {}

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Split the index
# html_split_index = False


# Options for LaTeX output
# ------------------------
latex_elements = {'inputenc': r'\usepackage[utf8x]{inputenc}', 'utf8extra': ''}

# The paper size ('letter' or 'a4').
latex_elements['papersize'] = 'a4'

# The font size ('10pt', '11pt' or '12pt').
latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
latex_documents = [
    (
     'index',
     'DISCOS Documentation',
     'DISCOS CS team', 'manual'
    ),
]

pdf_break_level = 0

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

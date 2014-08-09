#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import sys
# import os

from colemaktutor import colemaktutor

project = 'colemaktutor'
copyright = '2014, Benjamin Althues'
release = version = colemaktutor.__version__

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build']
pygments_style = 'sphinx'

html_theme = 'nature'  # default, nature
#html_theme_options = {}
#html_theme_path = []
#html_title = None
#html_short_title = None
#html_logo = None
#html_favicon = None
html_static_path = ['_static']
#html_extra_path = []
html_show_sourcelink = False

htmlhelp_basename = 'colemaktutordoc'

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'preamble': '',
}
latex_documents = [
    ('index', 'colemaktutor.tex', 'colemaktutor Documentation',
     'Benjamin Althues', 'manual'),
]
#latex_logo = None
#latex_use_parts = False
#latex_show_pagerefs = False
#latex_show_urls = False
#latex_appendices = []
#latex_domain_indices = True

man_pages = [
    ('index', 'colemaktutor', 'colemaktutor Documentation',
     ['Benjamin Althues'], 1)
]
#man_show_urls = False

texinfo_documents = [
    ('index', 'colemaktutor', 'colemaktutor Documentation',
     'Benjamin Althues', 'colemaktutor', 'One line description of project.',
     'Miscellaneous'),
]

epub_title = 'colemaktutor'
epub_author = 'Benjamin Althues'
epub_publisher = 'Benjamin Althues'
epub_copyright = '2014, Benjamin Althues'
#epub_basename = 'colemaktutor'
epub_exclude_files = ['search.html']
#epub_tocdepth = 3
#epub_tocdup = True
#epub_tocscope = 'default'
#epub_fix_images = False
#epub_max_image_width = 0
#epub_show_urls = 'inline'
#epub_use_index = True

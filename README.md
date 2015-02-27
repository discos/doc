DISCOS Documentation
====================
This directory contains the reStructuredText (reST) sources to the DISCOS
documentation.  You don't need to build them yourself, prebuilt versions are
available [here](http://discos.readthedocs.org/).


Building the docs
-----------------
You need to have [Sphinx](http://sphinx-doc.org/) installed; it is the toolset
used to build the docs. A Makefile has been prepared so that on Unix, provided 
you have installed Sphinx, you can just run:

```
make html
```

to build the HTML output files. Available make targets are:

- **clean**, which removes all build files.
- **html**, which builds standalone HTML files for offline viewing.
- **latex**, which builds LaTeX source files as input to "pdflatex" to produce 
  PDF documents.
- **text**, which builds a plain text file for each source file.
- **epub**, which builds an EPUB document, suitable to be viewed on e-book
  readers.

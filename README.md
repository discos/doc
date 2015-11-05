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

<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">DISCOS documentation</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://discos.readthedocs.org/en/latest/about/people.html" property="cc:attributionName" rel="cc:attributionURL">the DISCOS team</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.

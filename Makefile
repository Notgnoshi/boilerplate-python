# Minimal makefile for Sphinx documentation
#
.PHONY: help Makefile

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = Boilerplate
SOURCEDIR     = docs
BUILDDIR      = docs/build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

viewhtml: html
	firefox docs/build/html/index.html

viewlatex: latexpdf
	xdg-open docs/build/latex/$(SPHINXPROJ).pdf

check:
	@nosetests                                                                 \
		--processes=-1                                                         \
		--with-doctest                                                         \
		--with-coverage                                                        \
		--cover-html                                                           \
		--cover-erase                                                          \
		--cover-tests                                                          \
		--cover-inclusive                                                      \
		--cover-package=boilerplate                                            \
		--cover-html-dir=htmlcov

viewcoverage: check
	firefox htmlcov/index.html

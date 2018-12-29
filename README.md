# Boilerplate Python Project

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Unit tests

Run unit tests with the provided `runtests.py` script. Alternatively, run them with `nosetests --with-doctests`. There are unit tests in the `boilerplate.tests` submodule, and there are doctests throughout the `boilerplate` module.

## Documentation

I've never used Sphinx in an actual project before (it's been on the TODO list though) so it may not be configured quite right. To write the documentation, edit the `docs/*.rst` files to your liking, then build the documentation. I recommend one of two ways:

* HTML: `make html` then `make viewhtml`
* LaTeX: `make latex` then `make viewlatex`

Simply running `make` will display the options available.

## Dependencies

* `nose`
* `Sphinx` and `sphinxcontrib-napoleon`
* `doctest`
* Python 3.6+

## TODO

* Get `setup.py` figured out
* Make a `requirements.txt`
* Document how to configure Sphinx
* Add runtests and view code coverage to `Makefile`.

# Boilerplate Python Project

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Unit tests

Run unit tests with `make runtests`. There are unit tests in the `boilerplate.tests` submodule, and
there are doctests throughout the `boilerplate` module. The code coverage results are viewable with
`make viewcoverage`.

## Documentation

I've never used Sphinx in an actual project before (it's been on the TODO list though) so it may not
be configured quite right. To write the documentation, edit the `docs/*.rst` files to your liking,
then build the documentation. I recommend one of two ways:

* HTML: `make html` then `make viewhtml`
* LaTeX: `make latex` then `make viewlatex`

Simply running `make` will display the options available.

## TODO

* Get `setup.py` fully figured out
* Document how to configure Sphinx

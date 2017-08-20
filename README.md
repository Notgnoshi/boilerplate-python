# Boilerplate Python Project

## Unit tests

Run unit tests with the provided `runtests.py` script. Alternatively, run them with `nosetests --with-doctests`. There are unit tests in the `boilerplate.tests` submodule, and there are doctests throughout the `boilerplate` module.

## Documentation

I've never used Sphinx in an actual project before (it's been on the TODO list though) so it may not be configured quite right. To write the documentation, edit the `docs/*.rst` files to your liking, then build the documentation. I recommend one of two ways:

* HTML: `make html` then `make viewhtml`
* LaTeX: `make latex` then `make viewlatex`

Simply running `make` will display the options available.

## `setup.py`

This is something that I'm unsure about, but I have a `setup.py` file and I *think* it is bug-free (great, now I've guaranteed it doesn't work right ;) ).

## Dependencies

TODO: There's a way to install all the dependencies using the `setup.py` file. However, until I figure that out, here are the dependencies:

* `nose`
* `Sphinx`
* `doctest`
* Python 3.6+

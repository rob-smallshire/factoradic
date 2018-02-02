factoradic
==========

The *factorial number system* (also known as *factoradic*) is a way of
representing an integer as the sum of multiples of factorials. All
integers have a unique representation in the factoradic number system.
For example, the number 1337 can be represented as:

    1*6! + 5*5! + 0*4! + 2*3! + 2*2! + 1*1! + 0*0!

with coefficients 1 5 0 2 2 1 0. This is the unqiue factoradic
representation of decimal 1337.

Factoradic numbers have uses in combinatorics, particularly in the
numbering of permutations. This ``factoradic`` library is useful for
converting to and from factoradic number representations both in
Python and from the command-line.

Status
------

.. image:: https://travis-ci.org/rob-smallshire/factoradic.svg?branch=master
    :target: https://travis-ci.org/rob-smallshire/factoradic
    
.. image:: https://coveralls.io/repos/github/rob-smallshire/factoradic/badge.svg?branch=master
    :target: https://coveralls.io/github/rob-smallshire/factoradic?branch=master



Installation
------------

The ``factoradic`` package is available on the Python Package Index (PyPI):

.. image:: https://badge.fury.io/py/factoradic.svg
    :target: https://badge.fury.io/py/factoradic

The package supports Python 3 only. To install::

  $ pip install renard

Python Interface
----------------

For full help::

  >>> import factoradic
  >>> help(factoradic)

In the meantime, here are some highlights.

To convert from an integer to factoradic use ``to_factoradic()``::

  >>> from factoradic import to_factoradic
  >>> factoradic.to_factoradic(1337)
  [0, 1, 2, 2, 0, 5, 1]

The result is the list of coefficients where the factorial of each
zero-based index gives a place value, and the item at that index is
the coefficient by with the place value is to be multiplied. The
elements are from least-significant to most-significant. Since the
coefficient at any index must be less that or equal to the index,
the coefficient at index 0 is always 0.

To convert from factoradic use ``from_factoradic()``::

  >>> from factoradic import from_factoradic
  >>> factoradic.from_factoradic([0, 1, 2, 2, 0, 5, 1])
  1337


Command-Line Interface
----------------------

There's also a handy command-line interface. Run ``factoradic --help``
to see a list of commands::

  $ factoradic --help
  Factoradic.

  Convert to and from the factorial number system.

  Usage:
    factoradic from-integer <integer> [--expression]
    factoradic to-integer <coefficient-0> [<coefficient-1> [<coefficient-n>...]]

  Options:
    -e --expression  Show as a mathematical expression.


To convert from an integer to factoradic, use the ``from-integer`` subcommand::

  $ factoradic from-integer 1729
  0 1 0 0 2 2 2

The coefficients are reported from least-significant to most-significant.
The see the results as a math expression, specify the ``--expression`` flag::

  $ factoradic from-integer 1729 --expression
  2*6! + 2*5! + 2*4! + 0*3! + 0*2! + 1*1! + 0*0!

To convert from factoradic representation use the ``to-integer`` subcommand,
specifying the coefficients from least-significant to most-significant::

  $ factoradic to-integer 0 1 0 0 2 2 2
  1729

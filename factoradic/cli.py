"""Factoradic.

Convert to and from the factorial number system.

Usage:
  factoradic from-integer <integer> [--expression]
  factoradic to-integer <coefficient-0> [<coefficient-1> [<coefficient-n>...]]

Options:
  -e --expression  Show as a mathematical expression.
"""
import os
import sys

from docopt import docopt

import factoradic.convert


def reverse_enumerate(seq):
    return zip(range(len(seq) - 1, -1, -1), reversed(seq))


def from_integer(args):
    assert args['from-integer']

    try:
        n = int(args['<integer>'])
    except ValueError:
        print("'{}' is not an integer".format(args['<integer>']),
              file=sys.stderr)
        return os.EX_DATAERR

    coefficients = factoradic.convert.to_factoradic(n)

    if args['--expression']:
        print(' + '.join('{}*{}!'.format(c, i) for i, c in reverse_enumerate(coefficients)))
    else:
        print(' '.join(map(str, coefficients)))
    return os.EX_OK



def from_coefficients(args):
    assert args['to-integer']

    text_coefficients = [args['<coefficient-0>']]
    if args['<coefficient-1>'] is not None:
        text_coefficients.append(args['<coefficient-1>'])
    text_coefficients.extend(args['<coefficient-n>'])

    try:
        coefficients = list(map(int, text_coefficients))
    except ValueError:
        print("Not all coefficients in {} are integers".format(' '.join(text_coefficients)),
              file=sys.stderr)
        return os.EX_DATAERR

    try:
        value = factoradic.convert.from_factoradic(coefficients)
    except ValueError as e:
        print(e, file=sys.stderr)
        return os.EX_DATAERR

    print(value)
    return os.EX_OK


def main(argv=None):
    args = docopt(__doc__, argv=argv)
    if args['from-integer']:
        return from_integer(args)
    elif args['to-integer']:
        return from_coefficients(args)


if __name__ == '__main__':
    sys.exit(main())
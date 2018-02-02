from collections import OrderedDict
from numbers import Integral

from hypothesis import given, assume
from hypothesis.strategies import integers, floats
from math import factorial
from pytest import raises

from factoradic.convert import from_factoradic, to_factoradic


def test_0():
    assert to_factoradic(0) == [0]


def test_1():
    assert to_factoradic(1) == [0, 1]


def test_2():
    assert to_factoradic(2) == [0, 0, 1]


def test_3():
    assert to_factoradic(3) == [0, 1, 1]


def test_4():
    assert to_factoradic(4) == [0, 0, 2]


def test_5():
    assert to_factoradic(5) == [0, 1, 2]


def test_6():
    assert to_factoradic(6) == [0, 0, 0, 1]


@given(n=integers(min_value=0))
def test_roundtrip(n):
    assert from_factoradic(to_factoradic(n)) == n


@given(n=integers(min_value=0))
def test_first_place_is_always_zero(n):
    assert to_factoradic(n)[0] == 0


@given(n=integers(min_value=0))
def test_coefficients_are_less_than_or_equal_to_index(n):
    assert all(coefficient <= index for index, coefficient in enumerate(to_factoradic(n)))


@given(n=integers(max_value=-1))
def test_negative_integers_raise_value_error(n):
    with raises(ValueError):
        to_factoradic(n)


@given(n=floats(min_value=0, allow_nan=False, allow_infinity=False))
def test_non_integers_raise_value_error(n):
    assume(int(n) != n)
    with raises(ValueError):
        to_factoradic(n)


def test_nan_raises_value_error():
    with raises(ValueError):
        to_factoradic(float('nan'))


def test_infinity_raises_value_error():
    with raises(ValueError):
        to_factoradic(float('Inf'))


def test_empty_coefficients_raises_value_error():
    with raises(ValueError):
        from_factoradic([])


def test_out_of_range_coefficients_raise_value_error():
    with raises(ValueError):
        from_factoradic([1])

@given(m=integers(min_value=1, max_value=100))
def test_max_factoradic_is_one_less_than_factorial(m):
    assert from_factoradic(range(m)) == factorial(m) - 1

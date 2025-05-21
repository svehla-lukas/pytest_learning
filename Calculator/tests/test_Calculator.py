import math
import pytest

import sys, os

from calculator.Calculator import Calculator  # teď to najde src/Calculator.py


# ----------   fixture   ---------- #
@pytest.fixture()
def calc():
    """Returns a fresh calculator instance for each test."""
    return Calculator()


# ----------   parameterized tests   ---------- #
@pytest.mark.classicFunctionality
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 2),
        (3.14, -1.72, 1.42),
        (1 / 3, 1 / 3, 2 / 3),
        (2**63, 1, 2**63),
    ],
)
def test_add(calc, a, b, expected):
    assert math.isclose(calc.add(a, b), expected, rel_tol=1e-9)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 0),
        (3.14, -1.72, 4.86),
        (1 / 3, -1 / 3, 2 / 3),
        (2**63, 1, 2**63),
    ],
)
def test_subtract(calc, a, b, expected):
    assert math.isclose(calc.subtract(a, b), expected, rel_tol=1e-9)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 2),
        (3.14, -1.72, -5.4008),
        (1 / 3, 1 / 3, 1 / 9),
        (2**63, 1, 2**63),
    ],
)
def test_multiply(calc, a, b, expected):
    assert math.isclose(calc.multiply(a, b), expected, rel_tol=1e-9)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 1),
        (5, 5, 3125),
        (5, 1 / 3, 1.709975947),
        (-5, 3, -125),
        (2**63, 1, 2**63),
    ],
)
def test_power(calc, a, b, expected):
    assert math.isclose(calc.power(a, b), expected, rel_tol=1e-9)


# ----------   exception test   ---------- #
@pytest.fixture(params=["add", "subtract", "multiply", "power"])
def bad_method(calc, request):
    return getattr(calc, request.param)


@pytest.mark.string_input
@pytest.mark.parametrize(
    "a,b",
    [
        ("a", 1),
        (1, "b"),
        ("c", "d"),
    ],
)
def test_string_input(bad_method, a, b):
    with pytest.raises(TypeError) as excinfo:
        bad_method(a, b)
    assert str(excinfo.value) == "Both arguments must be numbers"


# ----------   exception test   ---------- #
@pytest.mark.edge
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (math.inf, 1, math.inf),
        (-math.inf, 2, -math.inf),
        (1.0, math.nan, math.nan),
        (2**63, 1, 2**63),  # extreme int
    ],
    ids=["inf", "neg_inf", "nan", "extreme_int"],
)
def test_divide_edge(a, b, expected):
    calc = Calculator()
    result = calc.divide(a, b)
    # for NaN must be is_nan, because NaN != NaN
    if math.isnan(expected):
        assert math.isnan(result)
    else:
        assert result == expected


def test_divide_by_zero_raises(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(2, 0)

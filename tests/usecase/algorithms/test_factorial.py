import pytest
from src.usecase.algorithms.factorial.iteration import dp_factorial
from src.usecase.algorithms.factorial.recursive import factorial_recursive
from src.usecase.errors.math_errors import DomainOfDefinitionError


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
        (7, 5040),
        (8, 40320),
        (9, 362880),
        (10, 3628800),
    ],
)
def test_dp_factorial(n, expected):
    assert dp_factorial(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
        (7, 5040),
        (8, 40320),
        (9, 362880),
        (10, 3628800),
    ],
)
def test_recursive_factorial(n, expected):
    assert factorial_recursive(n) == expected


def test_dp_factorial_negative_error():
    with pytest.raises(DomainOfDefinitionError):
        dp_factorial(-1)


def test_recursive_factorial_negative_error():
    with pytest.raises(DomainOfDefinitionError):
        factorial_recursive(-1)

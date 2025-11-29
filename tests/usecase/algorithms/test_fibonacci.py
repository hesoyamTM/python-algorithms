import pytest
from src.usecase.algorithms.fibonacci.iteration import dp_fibonacci
from src.usecase.algorithms.fibonacci.recursive import recursive_fibonacci
from src.usecase.algorithms.fibonacci.matrix_power import fibonacci_matrix
from src.usecase.errors.math_errors import DomainOfDefinitionError


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (6, 13),
        (7, 21),
        (8, 34),
        (9, 55),
        (10, 89),
    ],
)
def test_dp_fibonacci(n, expected):
    assert dp_fibonacci(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (6, 13),
        (7, 21),
        (8, 34),
        (9, 55),
        (10, 89),
    ],
)
def test_recursive_fibonacci(n, expected):
    assert recursive_fibonacci(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (6, 13),
        (7, 21),
        (8, 34),
        (9, 55),
        (10, 89),
    ],
)
def test_matrix_power_fibonacci(n, expected):
    assert fibonacci_matrix(n) == expected


def test_dp_fibonacci_negative_error():
    with pytest.raises(DomainOfDefinitionError):
        dp_fibonacci(-1)


def test_recursive_fibonacci_negative_error():
    with pytest.raises(DomainOfDefinitionError):
        recursive_fibonacci(-1)


def test_matrix_power_fibonacci_negative_error():
    with pytest.raises(DomainOfDefinitionError):
        fibonacci_matrix(-1)

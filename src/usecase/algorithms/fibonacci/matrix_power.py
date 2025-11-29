from src.usecase.errors.math_errors import DomainOfDefinitionError
from loguru import logger


class Matrix2x2:
    value: list[list[int]]

    def __init__(self, value: list[list[int]]):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self.value)


def multiply(a: Matrix2x2, b: Matrix2x2) -> Matrix2x2:
    """
    Multiplies two matrices
    :param a: First matrix
    :param b: Second matrix
    :return: The product of the two matrices
    """

    logger.debug(f"Multiplying {a} and {b}")

    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a.value[i][k] * b.value[k][j]

    logger.debug(f"Multiplication of {a} and {b} is {result}")
    return Matrix2x2(result)


def binary_power(a: Matrix2x2, n: int) -> Matrix2x2:
    """
    Calculates the power of a matrix
    :param a: Matrix
    :param n: Power
    :return: The power of the matrix
    """

    logger.debug(f"Calculating power of {a} to the power of {n}")

    result = Matrix2x2([[1, 0], [0, 1]])

    while n > 0:
        if n & 1:
            result = multiply(result, a)
        a = multiply(a, a)
        n >>= 1

    logger.debug(f"Power of {a} to the power of {n} is {result}")
    return result


def fibonacci_matrix(n: int) -> int:
    """
    Calculates the nth Fibonacci number
    :param n: The number
    :return: The nth Fibonacci number
    """

    logger.debug(f"Calculating Fibonacci of {n}")

    if n < 0:
        logger.error("Fibonacci is not defined for negative numbers")
        raise DomainOfDefinitionError("Fibonacci is not defined for negative numbers")

    matrix = binary_power(Matrix2x2([[1, 1], [1, 0]]), n)

    logger.debug(f"Fibonacci of {n} is {matrix.value[0][0]}")
    return matrix.value[0][0]

from src.usecase.errors.math_errors import DomainOfDefinitionError
from loguru import logger


def dp_fibonacci(n: int) -> int:
    """
    Calculates the nth Fibonacci number using dynamic programming
    :param n: The number
    :return: The nth Fibonacci number
    """

    logger.debug(f"Calculating Fibonacci of {n}")

    if n < 0:
        logger.error("Fibonacci is not defined for negative numbers")
        raise DomainOfDefinitionError("Fibonacci is not defined for negative numbers")

    a = b = 1
    for _ in range(n):
        a, b = b, a + b

    logger.debug(f"Fibonacci of {n} is {a}")
    return a

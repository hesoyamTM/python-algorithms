from src.usecase.errors.math_errors import DomainOfDefinitionError
from loguru import logger


def recursive_fibonacci(n: int) -> int:
    """
    Calculates the nth Fibonacci number using recursion
    :param n: The number
    :return: The nth Fibonacci number
    """

    logger.debug(f"Calculating Fibonacci of {n}")

    if n < 0:
        logger.error("Fibonacci is not defined for negative numbers")
        raise DomainOfDefinitionError("Fibonacci is not defined for negative numbers")

    res: int
    if n == 0:
        res = 1
    if n == 1:
        res = 1
    else:
        res = recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

    logger.debug(f"Fibonacci of {n} is {res}")
    return res

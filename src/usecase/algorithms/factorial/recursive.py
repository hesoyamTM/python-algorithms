from src.usecase.errors.math_errors import DomainOfDefinitionError
from loguru import logger


def factorial_recursive(n: int) -> int:
    """
    Calculates the factorial of a number using recursion
    :param n: The number
    :return: The factorial of the number
    """

    logger.debug(f"Calculating factorial of {n}")

    if n < 0:
        logger.error("Factorial is not defined for negative numbers")
        raise DomainOfDefinitionError("Factorial is not defined for negative numbers")

    res = 1
    if n > 0:
        res = n * factorial_recursive(n - 1)

    logger.debug(f"Factorial of {n} is {res}")
    return res

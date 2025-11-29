from src.usecase.errors.math_errors import DomainOfDefinitionError
from loguru import logger


def dp_factorial(n: int) -> int:
    """
    Calculates the factorial of a number using dynamic programming
    :param n: The number
    :return: The factorial of the number
    """

    logger.debug(f"Calculating factorial of {n}")

    if n < 0:
        logger.error("Factorial is not defined for negative numbers")
        raise DomainOfDefinitionError("Factorial is not defined for negative numbers")

    arr = [1] * (n + 1)
    for i in range(1, n + 1):
        arr[i] = i * arr[i - 1]

    logger.debug(f"Factorial of {n} is {arr[n]}")
    return arr[n]

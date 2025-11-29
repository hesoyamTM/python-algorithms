from typing import Callable, Any
from src.constants import C, T

from loguru import logger


def quick_sort(
    arr: list[T],
    key: Callable[[T], Any] = lambda x: x,
    cmp: Callable[[C, C], int] = lambda x, y: -1 if x < y else 1 if x > y else 0,
) -> list[T]:
    """
    Sorts an array using quick sort
    :param arr: The array to sort
    :return: The sorted array
    """

    logger.debug(f"Sorting array {arr} using quick sort")

    if len(arr) <= 1:
        return arr

    left, right, pivot = [], [], arr[0]

    for i in range(1, len(arr)):
        if cmp(key(arr[i]), key(pivot)) <= 0:
            left.append(arr[i])
        elif cmp(key(arr[i]), key(pivot)) > 0:
            right.append(arr[i])

    result = quick_sort(left, key, cmp) + [pivot] + quick_sort(right, key, cmp)
    logger.debug(f"Result array {result} using quick sort")

    return result


if __name__ == "__main__":
    import random

    arr = list(range(10))
    random.shuffle(arr)

    print(f"Original array: {arr}")
    print(f"Sorted array: {quick_sort(arr)}")
    print(f"Reverse sorted array: {quick_sort(arr, key=lambda x: -x)}")

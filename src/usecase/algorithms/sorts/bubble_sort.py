from typing import Callable, Any
from src.constants import C, T
from loguru import logger


def bubble_sort(
    arr: list[T],
    key: Callable[[T], Any] = lambda x: x,
    cmp: Callable[[C, C], int] = lambda x, y: -1 if x < y else 1 if x > y else 0,
) -> list[T]:
    """
    Sorts an array using bubble sort
    :param arr: The array to sort
    :return: The sorted array
    """

    logger.debug(f"Sorting array {arr} using bubble sort")

    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if cmp(key(arr[j]), key(arr[j + 1])) > 0:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    logger.debug(f"Result array {arr} using bubble sort")

    return arr


if __name__ == "__main__":
    import random

    arr: list[int] = list(range(10))
    random.shuffle(arr)

    print(f"Original array: {arr}")
    print(f"Sorted array: {bubble_sort(arr)}")
    print(f"Reverse sorted array: {bubble_sort(arr, key=lambda x: -x)}")
    print(
        f"Sorted array with reverse key: {bubble_sort(arr, key=lambda x: -x, cmp=lambda x, y: 1 if x < y else -1)}"
    )

from typing import Callable, Any
from src.constants import C, T
from loguru import logger


def heapify(
    arr: list[T],
    n: int,
    i: int,
    key: Callable[[T], Any] = lambda x: x,
    cmp: Callable[[C, C], int] = lambda x, y: -1 if x < y else 1 if x > y else 0,
) -> None:
    """
    Heapifies an array
    :param arr: The array to heapify
    :param n: The length of the array
    :param i: The index of the element to heapify
    """

    logger.debug(f"Heapifying array {arr} at index {i}")

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and cmp(key(arr[left]), key(arr[largest])) > 0:
        largest = left

    if right < n and cmp(key(arr[right]), key(arr[largest])) > 0:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(
    arr: list[T],
    key: Callable[[T], Any] = lambda x: x,
    cmp: Callable[[C, C], int] = lambda x, y: -1 if x < y else 1 if x > y else 0,
) -> list[T]:
    """
    Sorts an array using heap sort
    :param arr: The array to sort
    :return: The sorted array
    """

    logger.debug(f"Sorting array {arr} using heap sort")

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key, cmp)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, key, cmp)

    logger.debug(f"Result array {arr} using heap sort")

    return arr


if __name__ == "__main__":
    import random

    arr = list(range(10))
    random.shuffle(arr)

    print(f"Original array: {arr}")
    print(f"Sorted array: {heap_sort(arr)}")
    print(f"Reverse sorted array: {heap_sort(arr, key=lambda x: -x)}")
    print(
        f"Sorted array with reverse key: {heap_sort(arr, key=lambda x: -x, cmp=lambda x, y: 1 if x < y else -1)}"
    )

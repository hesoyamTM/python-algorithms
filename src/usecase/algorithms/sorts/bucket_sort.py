from loguru import logger


def bucket_sort(arr: list[float], num_buckets: int = 10) -> list[float]:
    """
    Sorts an array using bucket sort
    :param arr: The array to sort
    :param num_buckets: The number of buckets to use
    :return: The sorted array
    """

    mx, mn = max(arr), min(arr)

    return _recursive_bucket_sort(arr, mn, mx, num_buckets)


def _recursive_bucket_sort(
    arr: list[float],
    min_element: float,
    max_element: float,
    num_buckets: int,
) -> list[float]:
    """
    Recursively sorts an array using bucket sort
    :param arr: The array to sort
    :param num_buckets: The number of buckets to use
    :return: The sorted array
    """

    logger.debug(f"Sorting array {arr} using bucket sort")

    if len(arr) < 2 or min_element == max_element:
        return arr

    range_arr = max_element - min_element
    buckets: list[list[float]] = [[] for _ in range(num_buckets)]
    min_elements: list[float] = [float("inf")] * num_buckets
    max_elements: list[float] = [float("-inf")] * num_buckets

    for element in arr:
        index: int = int((element - min_element) / range_arr * (num_buckets - 1))
        buckets[index].append(element)
        min_elements[index] = min(min_elements[index], element)
        max_elements[index] = max(max_elements[index], element)

    for i in range(num_buckets):
        buckets[i] = _recursive_bucket_sort(
            buckets[i],
            min_elements[i],
            max_elements[i],
            num_buckets,
        )

    result: list[float] = [0] * len(arr)
    k = 0

    for i in buckets:
        for j in i:
            result[k] = j
            k += 1

    logger.debug(f"Sorted array {arr} using bucket sort")
    return result


if __name__ == "__main__":
    import random

    arr = [random.uniform(-10, 10) for _ in range(10)]
    random.shuffle(arr)

    print(f"Original array: {arr}")
    print(f"Sorted array: {bucket_sort(arr)}")

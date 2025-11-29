from loguru import logger


def counting_sort(arr: list[int]) -> list[int]:
    """
    Sorts an array using counting sort
    :param arr: The array to sort
    :return: The sorted array
    """

    logger.debug(f"Sorting array {arr} using counting sort")

    max_value = max(arr)
    min_value = min(arr)

    count = [0] * (max_value - min_value + 1)

    for i in arr:
        count[i - min_value] += 1

    result = []
    for i in range(len(count)):
        for _ in range(count[i]):
            result.append(i + min_value)

    logger.debug(f"Result array {result} using counting sort")
    return result


if __name__ == "__main__":
    import random

    arr = [int(random.uniform(-10, 10)) for _ in range(10)]
    random.shuffle(arr)
    print(f"Original array: {arr}")
    print(f"Sorted array: {counting_sort(arr)}")

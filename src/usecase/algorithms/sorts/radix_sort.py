from loguru import logger


def radix_lsd_sort(arr: list[int], base: int = 10) -> list[int]:
    """
    Sorts an array using radix sort
    :param arr: The array to sort
    :return: The sorted array
    """

    logger.debug(f"Sorting array {arr} using radix sort")

    buckets = [[] for _ in range(base)]
    mx = max(arr)
    cur = 0

    while mx > 0:
        for i in arr:
            buckets[(i // base**cur) % base].append(i)

        k = 0
        for i in range(base):
            for j in buckets[i]:
                arr[k] = j
                k += 1
            buckets[i].clear()

        mx //= base
        cur += 1

    logger.debug(f"Result array {arr} using radix sort")

    return arr


if __name__ == "__main__":
    import random

    arr = list([random.randint(0, 100000) for _ in range(10000000)])
    random.shuffle(arr)

    print(f"Original array: {arr}")
    print(f"Sorted array: {radix_lsd_sort(arr, 10)}")

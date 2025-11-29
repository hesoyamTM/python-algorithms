import random


def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None) -> list[int]:
    """
    Generates a random array of integers
    :param n: The length of the array
    :param lo: The lower bound of the range
    :param hi: The upper bound of the range
    :param distinct: Whether the array should contain distinct values
    :param seed: The seed for the random number generator
    :return: The generated array
    """

    if seed is not None:
        random.seed(seed)

    arr = [random.randint(lo, hi) for _ in range(n)]

    if distinct:
        arr = list(set(arr))

        while len(arr) < n:
            arr.append(random.randint(lo, hi))
            arr = list(set(arr))

    return arr


def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    """
    Generates a nearly sorted array
    :param n: The length of the array
    :param swaps: The number of swaps to perform
    :param seed: The seed for the random number generator
    :return: The generated array
    """

    if seed is not None:
        random.seed(seed)

    arr = list(range(n))

    for _ in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr


def many_duplicates(n: int, k_unique=5, *, seed=None) -> list[int]:
    """
    Generates an array with many duplicates
    :param n: The length of the array
    :param k_unique: The number of unique values in the array
    :param seed: The seed for the random number generator
    :return: The generated array
    """

    if seed is not None:
        random.seed(seed)

    values = rand_int_array(k_unique, 0, n - 1, distinct=True, seed=seed)
    arr: list[int] = []

    while len(arr) < n:
        arr.append(random.choice(values))

    return arr


def reverse_sorted(n: int) -> list[int]:
    """
    Generates a reverse sorted array
    :param n: The length of the array
    :return: The generated array
    """

    arr = list(range(n))
    arr.reverse()
    return arr


def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None) -> list[float]:
    """
    Generates a random array of floats
    :param n: The length of the array
    :param lo: The lower bound of the range
    :param hi: The upper bound of the range
    :param seed: The seed for the random number generator
    :return: The generated array
    """

    if seed is not None:
        random.seed(seed)

    arr = [random.uniform(lo, hi) for _ in range(n)]
    return arr

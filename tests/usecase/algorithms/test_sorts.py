from src.usecase.algorithms.sorts.quick_sort import quick_sort
from src.usecase.algorithms.sorts.counting_sort import counting_sort
from src.usecase.algorithms.sorts.heap_sort import heap_sort
from src.usecase.algorithms.sorts.radix_sort import radix_lsd_sort as radix_sort
from src.usecase.algorithms.sorts.bubble_sort import bubble_sort
from src.usecase.algorithms.sorts.bucket_sort import bucket_sort
from random import randint, uniform


def test_quick_sort_random():
    for _ in range(100):
        arr = [randint(0, 100) for _ in range(10)]
        assert quick_sort(arr) == sorted(arr)


def test_counting_sort_random():
    for _ in range(100):
        arr = [randint(0, 100) for _ in range(10)]
        assert counting_sort(arr) == sorted(arr)


def test_heap_sort_random():
    for _ in range(100):
        arr = [randint(0, 100) for _ in range(10)]
        assert heap_sort(arr) == sorted(arr)


def test_radix_sort_random():
    for _ in range(100):
        arr = [randint(0, 100) for _ in range(10)]
        assert radix_sort(arr) == sorted(arr)


def test_bubble_sort_random():
    for _ in range(100):
        arr = [randint(0, 100) for _ in range(10)]
        assert bubble_sort(arr) == sorted(arr)


def test_bucket_sort_random():
    for _ in range(100):
        arr = [uniform(-10, 10) for _ in range(10)]
        assert bucket_sort(arr) == sorted(arr)

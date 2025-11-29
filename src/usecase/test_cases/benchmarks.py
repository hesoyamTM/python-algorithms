from typing import Callable


def timeit_once(func, *args, **kwargs) -> float:
    """
    Measures the time taken to execute a function once
    :param func: The function to measure
    :param args: The arguments to pass to the function
    :param kwargs: The keyword arguments to pass to the function
    :return: The time taken to execute the function once
    """

    import time

    start = time.time()
    func(*args, **kwargs)
    end = time.time()

    return end - start


def benchmark_sorts(
    arrays: dict[str, list], algos: dict[str, Callable]
) -> dict[str, dict[str, float]]:
    """
    Benchmarks the performance of sorting algorithms
    :param arrays: The arrays to benchmark
    :param algos: The sorting algorithms to benchmark
    :return: The benchmark results
    """

    results: dict[str, dict[str, float]] = {}
    for name, arr in arrays.items():
        results[name] = {}
        for algo_name, algo in algos.items():
            results[name][algo_name] = timeit_once(algo, arr)

    return results

#!/usr/bin/env python3
""" Measure the runtime """

from asyncio import run
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    A function named measure_time that measures the total execution time
    for wait_n(n, max_delay)

    Args:
        n (int): Number of times to wait a random delay.
        max_delay (int): Maximum delay in seconds.

    Returns:
        float: Average execution time per task.
    """
    start_time = time.time()
    run(wait_n(n, max_delay))
    total_time = time.time() - start_time

    return total_time / n

#!/usr/bin/env python3
""" Run time for four parallel comprehensions """

from time import perf_counter
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension four times
    in parallel using asyncio.gather.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = perf_counter()
    total_time = end_time - start_time

    return total_time

#!/usr/bin/env python3
""" Task """

import asyncio
from asyncio import Task
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asyncio Tasks to wait for random delays n times
    and return a list of the results.

    Args:
        n (int): Number of times to wait for a random delay.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of random delays.
    """
    delays = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*delays)

    return sorted(results)

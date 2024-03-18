#!/usr/bin/env python3
""" Tasks to await random delay time """

import asyncio
from asyncio import Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Asyncio Task that waits for a random delay
    between 0 and max_delay.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        Task: An asyncio Task representing the asynchronous operation.
    """
    return asyncio.create_task(wait_random(max_delay))

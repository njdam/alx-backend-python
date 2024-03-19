#!/usr/bin/env python3
""" A coroutine called async_generator that takes no arguments. """

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator coroutine that yields a random number between 0
    and 10 after waiting 1 second asynchronously, repeated 10 times.

    Yields:
        float: Random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.random() * 10  # Generates a sequence of 10 numbers

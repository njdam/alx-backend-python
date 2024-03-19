#!/usr/bin/env python3
""" Async Comprehensions """

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Async Comprehensions - The coroutine will collect 10 random numbers
    using an async comprehensing over async_generator and,
    then return the 10 random numbers.
    """
    rand_numbers = []
    async for num in async_generator():
        rand_numbers.append(num)

    return rand_numbers

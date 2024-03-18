#!/usr/bin/env python3
""" Let's execute multiple coroutines at the same time with async """

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Call wait_random with max_delay in n times
    and returns the list of all the delays
    """
    delay_list = []
    for _ in range(n):
        delay_list.append(wait_random(max_delay))

    return [await delay for delay in delay_list]

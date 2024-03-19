# Python - Async Comprehension

Python Async Comprehension is a Python library that demonstrates the usage of asynchronous comprehensions in Python.

## Installation

```bash
pip install python-async-comprehension
```

## Usage

To use Python Async Comprehension in your Python projects, import it as follows:
```python
from async_comprehension import async_comprehension
```

### Example

Here's an example of how you can use async comprehensions with Python Async Comprehension:
```python
import asyncio
from async_comprehension import async_comprehension

async def main():
    # Using async comprehension to fetch data asynchronously
    data = [i async for i in async_comprehension()]
    print(data)

asyncio.run(main())
```

## Documentation

### async_comprehension()

The `async_comprehension()` function is an asynchronous generator function that yields data asynchronously.

#### Example
```python
import asyncio
from async_comprehension import async_comprehension

async def main():
    # Using async comprehension to fetch data asynchronously
    data = [i async for i in async_comprehension()]
    print(data)

asyncio.run(main())
```

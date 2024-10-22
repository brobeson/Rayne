"""Unit test for rayne.py"""

from rayne import Benchmark


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))

benchmark = Benchmark()
benchmark(fibonacci, n=6)

"""Example use of PBench"""

from math import sqrt
from pbench import Benchmark


def closed_form(n: int) -> int:
    """
    Calculate F_n using the closed form equation.

    Args:
        n (int): Calculate the Fibonacci sequence value for this input.

    Returns:
        int: The Fibonacci sequence value for *n*.
    """
    phi = 1.6180339887
    psi = -0.6180339887
    return int((phi**n - psi**n) / sqrt(5))


def recursive(n: int) -> int:
    """
    Calculate F_n using the recursive formula.

    Args:
        n (int): Calculate the Fibonacci sequence value for this input.

    Returns:
        int: The Fibonacci sequence value for *n*.
    """
    if n == 1:
        return 1
    if n == 2:
        return 1
    return recursive(n - 1) + recursive(n - 2)


with Benchmark() as benchmark:
    benchmark.set_user_code(closed_form, n=5)

with Benchmark() as benchmark:
    benchmark.set_user_code(recursive, n=5)

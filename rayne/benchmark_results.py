"""Provide the BenchmarkResults class."""

from dataclasses import dataclass
from typing import List


@dataclass
class BenchmarkResults:
    """
    The results of running a microbenchmark

    The :py:class:`~rayne.benchmark.Benchmark` passes this object to the
    :py:mod:`~rayne.reporters` after it benchmarks the user code. Custom reporters must take
    one :py:class:`~rayne.benchmark_results.BenchmarkResults` object.

    Attributes:
        name: The results belong to the :py:class:`~rayne.benchmark.Benchmark` with this name.
        run_times: The list of execution times of the user code. Each entry is an integer number of
            nanoseconds. The length of this list should equal the number of benchmark
            :py:attr:`~rayne.benchmark.Benchmark.runs`.
    """

    name: str
    run_times: List[int]

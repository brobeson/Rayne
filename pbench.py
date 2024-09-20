"""Provide micro benchmarking functionality"""

import time
from statistics import fmean, stdev
from typing import List, Callable, Optional


class Benchmark:
    """
    Micro benchmark context manager

    Args:
        runs (int): Execute the test subject this many times. Each run is independently timed.
    """

    def __init__(self, runs: int = 1000):
        self.subject: Optional[Callable] = None
        self.__run_times: List[int] = []
        self.__runs = runs

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.subject is None:
            return False
        self.__run_benchmark()
        return True

    @property
    def mean(self) -> float:
        """
        Get the mean run time for the test subject.

        Returns:
            float: The mean of the measured run times.
        """
        return fmean(self.__run_times)

    @property
    def standard_deviation(self) -> float:
        """
        Get the standard deviation of the benchmark run times.

        Returns:
            float: The standard deviation of the benchmark run times.
        """
        return stdev(self.__run_times)

    def __run_benchmark(self):
        self.__run_times = [0 for _ in range(0, self.__runs)]
        for i in range(0, self.__runs):
            start_time = time.perf_counter_ns()
            self.subject()  # pylint:disable=not-callable
            end_time = time.perf_counter_ns()
            self.__run_times[i] = end_time - start_time

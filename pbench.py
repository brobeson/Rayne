"""Provide micro benchmarking functionality"""

import time
from statistics import mean, stdev
from typing import List, Callable, Optional, Dict, Any


class Benchmark:
    """
    Micro benchmark context manager

    Args:
        runs (int): Execute the test subject this many times. Each run is independently timed.
    """

    def __init__(self, runs: int = 1000):
        self.__user_function: Optional[Callable] = None
        self.__user_function_args: Dict[str, Any]
        self.__run_times: List[int] = []
        self.__runs = runs
        self.__clock_latency = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.__user_function is None:
            return False
        self.__measure_clock_latency()
        self.__run_benchmark()
        return True

    def set_user_code(self, function, **kwargs):
        """
        Set the user code to benchmark.

        Args:
            function (Callable): The benchmark measures the execution time of this function.
            kwargs: The benchmark passes these arguments to ``function``.
        """
        self.__user_function = function
        self.__user_function_args = kwargs

    @property
    def mean(self) -> float:
        """
        Get the mean run time for the test subject.

        Returns:
            float: The mean of the measured run times.
        """
        return mean(self.__run_times)

    @property
    def standard_deviation(self) -> float:
        """
        Get the standard deviation of the benchmark run times.

        Returns:
            float: The standard deviation of the benchmark run times.
        """
        return stdev(self.__run_times)

    def __measure_clock_latency(self):
        """
        Measure the clock latency

        It takes time to call time.perf_counter_ns(). A benchmark should not include that time
        within; it's not part of executing the function under test. This function measures the
        latency the same number of times as the benchmark runs, and stores the floor of the mean
        latency. Later, the benchmark will subtract this mean latency from each timing measurement.
        """
        total_latency = 0
        for _ in range(0, self.__runs):
            start_time = time.perf_counter_ns()
            end_time = time.perf_counter_ns()
            total_latency += end_time - start_time
        self.__clock_latency = total_latency // self.__runs

    def __run_benchmark(self):
        self.__run_times = [0 for _ in range(0, self.__runs)]
        for i in range(0, self.__runs):
            start_time = time.perf_counter_ns()
            self.__user_function(**self.__user_function_args)
            end_time = time.perf_counter_ns()
            self.__run_times[i] = max(end_time - start_time - self.__clock_latency, 0)

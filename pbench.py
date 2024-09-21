"""Provide micro benchmarking functionality"""

from dataclasses import dataclass
import time
from statistics import mean, stdev
from typing import List, Callable, Optional, Dict, Any


@dataclass
class BenchmarkResults:
    name: str
    run_times: List[int]


class Reporter:
    def report(self, result: BenchmarkResults):
        print(
            result.name,
            int(mean(result.run_times)),
            int(stdev(result.run_times)),
            sep="  ",
        )


class Benchmark:
    """
    Micro benchmark context manager

    Args:
        runs (int): Execute the test subject this many times. Each run is independently timed.
    """

    __next_benchmark_number = 1

    def __init__(
        self,
        name: Optional[str] = None,
        runs: int = 1000,
        reporter: Optional[Reporter] = None,
    ):
        if name:
            self.__name = name
        else:
            self.__name = f"Benchmark_{Benchmark.__next_benchmark_number}"
            Benchmark.__next_benchmark_number += 1
        self.__runs = runs
        if reporter is None:
            self.__reporter = Reporter()
        else:
            self.__reporter = reporter
        self.__user_function: Optional[Callable] = None
        self.__user_function_args: Dict[str, Any]
        self.__run_times: List[int] = []
        self.__clock_latency = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.__user_function is None:
            return False
        self.__measure_clock_latency()
        self.__run_benchmark()
        self.__make_report()
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

    def __make_report(self):
        self.__reporter.report(BenchmarkResults(self.__name, self.__run_times))

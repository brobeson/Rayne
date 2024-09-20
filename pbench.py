"""Provide micro benchmarking functionality"""

import time


class Benchmark:
    def __init__(self, runs: int = 1000):
        self.start_time = None
        self.end_time = None
        self.subject = None
        self.__runs = runs

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.subject is not None:
            self.__run_benchmark()
        return True

    @property
    def run_time(self):
        return self.end_time - self.start_time

    def __run_benchmark(self):
        self.start_time = time.perf_counter()
        for _ in range(0, self.__runs):
            self.subject()
        self.end_time = time.perf_counter()

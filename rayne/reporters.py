"""
Provide reporters to communicate benchmark results.

This module provides default reporters to communicate the results of a microbenchmark.
"""

import statistics
from .benchmark_results import BenchmarkResults


def mean_and_std_dev(results: BenchmarkResults) -> None:
    """
    Report the mean and standard deviation of the benchmark results.

    This reporter writes the data to standard output in a pseudo-table format.

    Args:
        results (BenchmarkResults): The results of running the benchmark.

    .. versionadded:: 0.2.0
    """
    print()
    print("Rayne Benchmark Results")
    if results.run_times:
        mean = int(statistics.fmean(results.run_times))
        stddev = int(statistics.stdev(results.run_times))
        width = max(len(str(mean)) + 3, len(str(stddev)) + 3, len(results.name))
        print(f"  name     {results.name:{width}}")
        print(f"  mean     {mean:{width-3}} ns")
        print(f"  std dev  {stddev:{width-3}} ns")
    else:
        width = max(len("n/a"), len(results.name))
        print(f"  name     {results.name:{width}}")
        print(f"  mean     {'n/a':{width}}")
        print(f"  std dev  {'n/a':{width}}")
        print("  No run times reported.")

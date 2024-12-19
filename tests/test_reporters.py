"""Unit tests for the reporters module."""

# cspell:words capsys
# pylint: disable=missing-function-docstring

from rayne import reporters
from rayne.benchmark_results import BenchmarkResults


def test_mean_and_std_dev(capsys) -> None:
    reporters.mean_and_std_dev(BenchmarkResults("Test", [5, 5, 5]))
    captured = capsys.readouterr()
    assert (
        captured.out == "\nRayne Benchmark Results\n"
        "  name     Test\n"
        "  mean     5 ns\n"
        "  std dev  0 ns\n"
    )


def test_mean_and_std_dev_empty_run_times(capsys) -> None:
    reporters.mean_and_std_dev(BenchmarkResults("Test", []))
    captured = capsys.readouterr()
    assert (
        captured.out == "\nRayne Benchmark Results\n"
        "  name     Test\n"
        "  mean     n/a \n"
        "  std dev  n/a \n"
        "  No run times reported.\n"
    )

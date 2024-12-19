Release Notes
=============

0.2.0
-----

New Features
............

#. Add the :py:func:`~rayne.reporters.mean_and_std_dev` basic reporter (:issue:`9`).

   This function prints the benchmark name, mean run time, and standard deviation to standard output.

0.1.0
-----

New Features
............

#. Add the :py:class:`~rayne.benchmark.Benchmark` class (:issue:`2`).

   Developers can write a micro-benchmark as a context manager.
   The manager benchmarks the user's function-under-test automatically during context exit.
#. Add the :py:class:`~rayne.benchmark_results.BenchmarkResults` class (:issue:`10`).

   Encapsulate benchmark results for later use by reporters.
#. Warm up the cache before benchmarking (:issue:`23`).

   Run the function-under-test before benchmarking.
   This loads code and data into the cache before measuring.

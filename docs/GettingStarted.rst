Getting Started
===============

First, import `Rayne`

.. code-block:: python
  
   from rayne import Benchmark

Rayne uses a context manager to run a micro benchmark.
In the context manager, set the benchmark ``subject`` to the function you want to benchmark.
When the context manager exits, it runs the benchmarks.

.. code-block:: python

   def fibonacci(n: int) -> int:
       # Calculate Fibonacci of 5.

   with Benchmark() as benchmark:
       benchmark.set_user_code(fibonacci, n=5)

By default, Rayne runs the subject 1000 times.
You can change this with the ``runs`` argument to ``Benchmark()``:

.. code-block:: python

   def fibonacci():
       # Calculate Fibonacci of 5.

   with Benchmark(runs=2000) as benchmark:
       benchmark.set_user_code(fibonacci, n=5)

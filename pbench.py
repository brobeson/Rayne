"""Micro benchmarking for Python functions."""

class Benchmark:
    def __call__(self, function, **kwargs):
        """
        Run the micro benchmark on a function.

        Args:
            function (callable): Benchmark this function.
            kwargs: The Benchmark passes these arguments to the ``function``.
        """
        function(**kwargs)

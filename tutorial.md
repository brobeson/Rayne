# Rayne Tutorial

> [!note]
> The commands in this tutorial are for Python 3 on Linux.
> For other platforms, adjust the commands accordingly.
> Rayne should work on any platform.

## Install Rayne

Start by installing Rayne.
Rayne is available through PyPI at <https://pypi.org/project/rayne/>.
Add it to your requirements or pyproject file, or install it manually with

```bash
pip3 install rayne
```

## Write Your Code

Rayne requires that your code be encapsulated in a `Callable` object.
For this tutorial, we'll benchmark two Fibonacci implementation: a recursive function and the closed form equation.[^1]

<https://github.com/brobeson/Rayne/blob/c3e1373a2929e76153858a06b42ce2d18c3b2a8d/fibonacci.py#L7-L36>

## Write Your Benchmarks

Rayne is designed around context managers.
Create your benchmark as a context manager and set it up within the context.
When the context exits, Rayne runs your code and measures the run time.

<https://github.com/brobeson/Rayne/blob/c3e1373a2929e76153858a06b42ce2d18c3b2a8d/fibonacci.py#L39-L43>

## Run Your Benchmarks

Run the benchmark script with Python.
By default, Rayne runs your code 1000 times.
The default reporter outputs the mean and standard deviation in nanoseconds.

```bash
$ python3 -m fibonacci
closed_form: μ=1351ns, σ=841ns
recursive: μ=1450ns, σ=337ns
```

[^1]: See <https://en.wikipedia.org/wiki/Fibonacci_sequence#Closed-form_expression>.

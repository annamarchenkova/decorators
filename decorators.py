import time
from functools import wraps

def timer(func):
  """
  Mesures tikme of function execution. Can be applied to any function that takes 
  any number of arguments and returns any value. Uses the functools.wraps decorator to 
  preserve the name and docstring of the original function.
  """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time of {func.__name__}: {end - start} seconds")
        return result
    return wrapper

# Example
@timer
def factorial(n):
    """Returns the factorial of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

@timer
def fibonacci(n):
    """Returns the nth Fibonacci number"""
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def debug(func):
  """
  Prints the name, arguments, and return value of the function.
  """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

# Example
@debug
def add(x, y):
    """Returns the sum of x and y"""
    return x + y

@debug
def greet(name, message="Hello"):
    """Returns a greeting message with the name"""
    return f"{message}, {name}!"

print(add(2, 3))
print(greet("Alice"))
print(greet("Bob", message="Hi"))

def memoize(func):
  """
  Caches the results of previous calls and returns them if 
  the same arguments are passed again, optimizing the performance of 
  recursive or expensive functions.
  """
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

# Example
@memoize
def factorial(n):
    """Returns the factorial of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
@memoize
def fibonacci(n):
    """Returns the nth Fibonacci number"""
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(factorial(10))
print(fibonacci(10))






























# 1. Timing Function Execution

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds")
        return result
    return wrapper
    
@timer
def example_function(n):
    time.sleep(n)
    
example_function(2)


# 2. Debugging Function Calls

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join([str(arg) for arg in args])
        kwargs_value = ", ".join([f"{key}={value}" for key, value in kwargs.items()])
        print(f"Calling {func.__name__} with args   {args_value} and with kwargs {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
@timer
def greet( name , greeting="Hello"):
    print(f"{greeting}, {name}")

greet("Aryan" , greeting="Good Morning")

# 3. Cache Return Value

def cache(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@cache
def expensive_func(n):
    time.sleep(2)
    return n**2

print(expensive_func(2))
print(expensive_func(3))
print(expensive_func(2))
# Define the decorator
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# Use the decorator on a function


@log_execution
def add(a, b):
    return a + b


@log_execution
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


# Call the decorated functions
result1 = add(2, 3)
result2 = greet("Alice", greeting="Hi")
result3 = greet("Bob")

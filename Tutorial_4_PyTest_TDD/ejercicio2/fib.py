def fibonacci(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fibonacci(n-1) + fibonacci(n-2)
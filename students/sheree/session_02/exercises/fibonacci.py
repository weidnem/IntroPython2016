def fibonacci(n):
    if n == 0:
        return 0
    elif  n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(1)
fibonacci(10)
fibonacci(100)
fibonacci(111111)
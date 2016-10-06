def fibonacci(n):
    """Establish bases and then find value at n"""
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)

print(fibonacci(5))


#def lucas(n):



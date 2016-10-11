"""Fibonacci series exercise"""

def fibonacci(n):
    fib_list = [0, 1]
    if len(fib_list) != n:
        fib_list.append(fib_list[(len(fib_list) - 2)] + fib_list[(len(fib_list) - 1)])
        fibonacci(n)
        print(len(fib_list))
        return len(fib_list)

    else:
        print(fib_list[n])
        return(fib_list[n])

fibonacci(5)
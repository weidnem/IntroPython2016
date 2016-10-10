"""
Name: Paul Briant
Date: 10/11/16
Class: Introduction to Python
LAB: Fibonacci

Description:

"""
# -------------------------------Import-----------------------------------------

# -------------------------------Functions--------------------------------------


def fibonacci(n):
    """
    Return the nth value in the Fibonacci series based on integer argument n.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)



# ==============================================================================


def main():
    """

    """
    print(fibonacci(3))
    print(fibonacci(2))
    print(fibonacci(0))
    print(fibonacci(7))

if __name__ == '__main__':
    main()

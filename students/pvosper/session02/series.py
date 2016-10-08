'''
    3rd LAB exercise from 161004

    Add a function called fibonacci.
    - The function should have one parameter n.
    - The function should return the nth value in the fibonacci series.
    - Ensure that your function has a well-formed docstring
    
    Add a function lucas that returns the nth value in the lucas numbers series.
    - Ensure that your function has a well-formed docstring
    
    Add a third function called sum_series with one required parameter and two 
    optional parameters. The required parameter will determine which element in
    the series to print. The two optional parameters will have default values
    of 0 and 1 and will determine the first two values for the series to be 
    produced.

    Calling this function with no optional parameters will produce numbers from
    the fibonacci series. Calling it with the optional arguments 2 and 1 will
    produce values from the lucas numbers. Other values for the optional
    parameters will produce other series.
    - Ensure that your function has a well-formed docstring
    
    Add a block of code to the end of your series.py module. Use the block to 
    write a series of assert statements that demonstrate that your three 
    functions work properly.

    Use comments in this block to inform the observer what your tests do.
'''

def fibonacci(n = 25):
    fib_list = [0, 1]
    for i in range(3,n+1):
        fib_list.append(fib_list[-1] + fib_list[-2])
    print("series: ", fib_list)
    return(fib_list[-1])

def lucas(n = 25):
    luc_list = [2, 1]
    for i in range(3,n+1):
        luc_list.append(luc_list[-1] + luc_list[-2])
    print("series: ", luc_list)
    return(luc_list[-1])

def sum_series(n = 25, sum0 = 0, sum1 = 1):
    sum_list = [sum0, sum1]
    for i in range(3,n+1):
        sum_list.append(sum_list[-1] + sum_list[-2])
        
    print("series: ", sum_list)
    return(sum_list[-1])
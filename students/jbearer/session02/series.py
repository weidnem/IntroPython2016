# Fibonacci Exercise
# Session02 - Oct. 5, 2016

def fibonacci(n):
    """ Fibonacci Series Exercise """
    for i in range(0, n):
        answer = (i-2) + (i-1)
        if answer <= 0:
            answer = 0
        if answer <= 1:
            answer = 1

        print(answer)

fibonacci(25)

#     answer = 0
#     if x == 0:
#         return 0
#     elif x == 1:
#         return 1
#     else:
#         answer = fibonacci(x-2) + fibonacci(x-1)
#     fibonacci(answer)

# fibonacci(5)

# answers = [fibonacci(x) for x in range(0, 1)]

# print(answers)

# print("Unendlicher Fibonacci-Generator Rekursiv")

# def fib(n):

#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


# row=[fib(n) for n in range(0,25)]
# print (row[-1])

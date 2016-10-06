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



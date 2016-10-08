'''
    2nd LAB exercise from 161004

    Write a program that prints the numbers from 1 to 100 inclusive.
    But for multiples of three print “Fizz” instead of the number
    For the multiples of five print “Buzz”.
    For numbers which are multiples of both three and five print “FizzBuzz” instead.
'''

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

for i in range(0,101):
    if i % 3 == 0 and i % 5 != 0:
        print("Fizz. This %d is a multiple of 3"% i )
    if i % 5 == 0 and i % 3 != 0:
        print("Buzz. This %d is a multiple of 5" % i)
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz. This %d  is divisible by 3 and 5." % i)
    elif i % 3 != 0 and i % 5 != 0:
        print(i)

def while_func(num, mystep):
    i = 0
    numbers = []

    while i < num:
        print ("At the top i is %d" % i)
        numbers.append(i)

        i = i + mystep
        print ("Numbers now: ", numbers)
        print ("At the bottom i is %d" % i)


    print ("The numbers: ")

    for num in numbers:
        print (num)

while_func(10,2)
# Charles Robison
# 2016.10.08
# Fizz Buzz

for i in range (101):
    if i == 0:
        continue
    elif (i % 3 == 0) and (i % 5 == 0):
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')

    else:
        print(i)
"""
Name: Paul Briant
Date: 10/11/16
Class: Introduction to Python
LAB: FIZZBUZZ

Description:
This program iterates through a range of numbers and prints each number. The
string 'Fizz' is printed for all numbers devisible by three. The string 'Buzz'
is printed for all numbers devisible by five. The string 'FizzBuzz' is printed
for all numbers devisible by both three and five.
"""
# -------------------------------Import-----------------------------------------

# -------------------------------Functions--------------------------------------

# ==============================================================================


def main():
    """
    
    """
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

if __name__ == '__main__':
    main()

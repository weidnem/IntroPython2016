# Raw Input Exercise #

# age = input("How old are you? ")
#
# height = input("How tall are you? ")
#
# weight = input("How much do you weigh? ")
#
# print('So, you\'re %r old, %r tall and %r heavy.' % (age, height, weight))

# Parameters, Unpacking, Variables #

from sys import argv

script, first, second, third , fourth = argv

print("The script is called:"), script
print("Your first variable is:"), first
print("Your second variable is:"), second
print("Your third variable is:"), third
print("Give me a fourth variable: "), fourth





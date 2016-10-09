# Raw Input Exercise #

# age = input("How old are you? ")
#
# height = input("How tall are you? ")
#
# weight = input("How much do you weigh? ")
#
# print('So, you\'re %r old, %r tall and %r heavy.' % (age, height, weight))

# Parameters, Unpacking, Variables #

# from sys import argv
#
# script, first, second, third , fourth = argv
#
# print("The script is called:"), script
# print("Your first variable is:"), first
# print("Your second variable is:"), second
# print("Your third variable is:"), third
# print("Give me a fourth variable: "), fourth

# from sys import argv
#
# script, user_name = argv
# prompt = 'Hmmmm? '
#
# print("Hi %s, I'm the %s script." % (user_name, script))
# print("I'd like to ask you a few questions.")
# print("Do you like me %s?" % (user_name))
# likes = input(prompt)
#
# print("What city do you live in %s?" % (user_name))
# lives = input(prompt)
#
# print("What kind of computer do you have?")
# computer = input(prompt)
#
# print("What part of the city do you live in?")
# city = input(prompt)
#
# print("""
# Alright, so you said %r about liking me.
# You live in %r.  Not sure where that is.
# And you have a %r computer and live in %r.  Nice.
# """ % (likes, lives, computer, city))

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))

# this just takes one argument
def print_one(arg1):
    print("arg1: %r" % (arg1))

# this one takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()






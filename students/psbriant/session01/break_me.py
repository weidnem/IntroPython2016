#Name: Paul Briant
#Date: 10/04/16
#Class: Introduction to Python
#Assignment: Session One
#
#Description:
#This program contains four functions, each which results in one of
#four common exceptions including the NameError, TypeError, SyntaxError, and
#AttributeError.

#-------------------------------------Imports-----------------------------------
import math
#------------------------------------Functions----------------------------------

#This function results in a NameError. Zero arguments are accepted and zero
#values are returned. A None statement is returned at the end of the function.
def name_error():
    name = input("Please enter your name: ")
    #your_name should be name
    print("Hello " + your_name +
    "! You are well on your way to becoming a coding ninja!")

    return None

#This function results in a TypeError. An int is the sole argument accepted and
#zero values are returned. A None statement is returned at the end of the
#function.
def type_error(number):
    while number > 2:
        #The operand '/' is not supported for the string '2'.
        number /= '2'
        print(number)

    return None

#This function results in a SyntaxError. Zero arguments are accepted and zero
#values are returned. A None statement is returned at the end of the function.
def syntax_error():
    name = input("Please enter your name: ")
    #The print statement requires parentheses in python 3.
    print "Hello " + name +
    "! You are well on your way to becoming a coding ninja!"

    return None

#This function results in a AttributeError. An int is the sole argument accepted
#and zero values are returned. A None statement is returned.
def attribute_error(number):
    #The function 'expo' does not exist for the math module.
    print(math.expo(number))

    return None

#===============================================================================
def main():

    name_error()
    type_error(20)
    syntax_error()
    attribute_error(2)

if __name__ == '__main__':
  main()

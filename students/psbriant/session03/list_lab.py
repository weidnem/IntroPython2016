# !/usr/bin/env python3

"""
Name: Paul Briant
Date: 10/11/16
Class: Introduction to Python
LAB: List Lab

Description:

"""
# -------------------------------Import-----------------------------------------

# -------------------------------Functions--------------------------------------
def series1(fruit):
    # Add some cool text formatting
    print(fruit)
    new_fruit = input("Please enter another fruit ")
    fruit.append(new_fruit)
    # Add some cool text formatting
    print(fruit)
    number = input("Please enter a number ")
    # Add some cool text formatting
    print(number, fruit(number))
    fruit = ["Watermelon"] + fruit
    # Add some cool text formatting
    print(fruit)
    fruit.insert("Pineapple", 0)
    # Add some cool text formatting
    print(fruit)




# ==============================================================================

def main():
    """

    """
    # fruit = ["Apples", "Pears", "Oranges", "Peaches"]
     # series1(fruit)


if __name__ == '__main__':
    main()

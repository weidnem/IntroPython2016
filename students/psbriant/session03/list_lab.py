# !/usr/bin/env python3

"""
Name: Paul Briant
Date: 10/11/16
Class: Introduction to Python
LAB: List Lab

Description:

"""
# -------------------------------Functions--------------------------------------


def series1(fruit):
    """
    Take in a list of strings and displays the original list before prompting
    the user to add additonal items to the list. The original list is modified
    based on user input and insertions to the beginning of the list.
    """
    print(fruit)
    # Prompts user for an additional fruit
    new_fruit = input("Please enter another fruit ")
    fruit.append(new_fruit)
    # Add some cool text formatting
    print(fruit)
    number = int(input("Please enter a number "))
    # Ask about 'one is first basis'.
    print(number, fruit[number])
    # Adds new fruit to beginning of list using concatenation
    fruit = ["Watermelon"] + fruit
    print(fruit)
    # Inserts new fruit at beginning of list
    fruit.insert(0, "Pineapple")
    print(fruit)
    # displays all fruits beginning with the letter 'P'
    for item in fruit:
        if item[0] == 'P':
            print(item)


def series2(fruit):
    """
    Take in a list of strings and diplays the original list before removing the
    last element of the list and prompting the user for a specific item to
    remove from the list.
    """
    print(fruit)
    # Remove last element from list
    del fruit[-1]
    print(fruit)
    # Prompts user for a fruit to remove from list
    to_delete = input("What fruit do you want deleted from this list? ")
    fruit.remove(to_delete)


def series3(fruit):
    """

    """
    for item in fruit:
        # Make item lowercase
        item.lower()
        # Asks the user whether they like each fruit
        preference = input("Do you like " + item + "? yes|no")
        # Checks to make sure user entered either 'yes' or 'no'
        if preference != 'no' and preference != 'yes':
            # Repeatedly prompts user to enter 'yes' or 'no' until they do.
            while True:
                preference = input("Please answer with either yes or no")
                if preference == 'yes' or preference == 'no':
                    return False
        if preference == 'no':
            # remove item from fruit
            fruit.remove(item)
    print(fruit)


def series4(fruit):
    """

    """
    # Create copy of fruit
    rev_fruit = fruit[:]
    # Iterate through copy of fruit and reverse each element
    for item in rev_fruit:
        # Reverse each element
        item[::-1]
    # Delete last item in original list
    del fruit[-1]
    print(fruit, rev_fruit)


# ==============================================================================


def main():
    """

    """
    # Create original list of fruit
    fruit = ["Apples", "Pears", "Oranges", "Peaches"]
    # series1(fruit)
    series2(fruit)


if __name__ == '__main__':
    main()

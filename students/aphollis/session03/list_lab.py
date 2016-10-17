#!/usr/bin/env python3

"""
When the script is run, it should accomplish the following four series of actions:

    -Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    -Display the list.
    -Ask the user for another fruit and add it to the end of the list.
    -Display the list.
    -Ask the user for a number and display the number back to the user and the fruit corresponding to that number
        (on a 1-is-first basis).
    -Add another fruit to the beginning of the list using “+” and display the list.
    -Add another fruit to the beginning of the list using insert() and display the list.
    -Display all the fruits that begin with “P”, using a for loop.

Using the list created in series 1 above:

    -Display the list.
    -Remove the last fruit from the list.
    -Display the list.
    -Ask the user for a fruit to delete and find it and delete it.
    (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)

Again, using the list from series 1:

    -Ask the user for input displaying a line like “Do you like apples?”
    -for each fruit in the list (making the fruit all lowercase).
    -For each “no”, delete that fruit from the list.
    -For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values
        (a while loop is good here):
    -Display the list.

Once more, using the list from series 1:

    -Make a copy of the list and reverse the letters in each fruit in the copy.
    -Delete the last item of the original list. Display the original list and the copy.

"""
def main(list=["Apples", "Pears", "Oranges", "Peaches"]):
    #aware that a mutable default is not ideal, but it works well for this exercise.

    display_list(list)
    a_new_one = input("Add another fruit! > ")

    #added ability to skip to speed up testing.
    if a_new_one == "2":
        """skip to part 2."""
        list = ["Kiwi", "Pomegranate", "Apples", "Pears", "Oranges", "Peaches", "Grapes"]
        part_deux(list)

    elif a_new_one == "3":
        """skip to part 3"""
        list = ["Kiwi", "Pomegranate", "Apples", "Pears", "Oranges", "Peaches", "Grapes"]
        part_three(list)

    elif a_new_one == "4":
        """skip to part 4"""
        list = ["Kiwi", "Pomegranate", "Apples", "Pears", "Oranges", "Peaches", "Grapes"]
        part_four(list)

    else:
        #series 1
        add_end(list, a_new_one)
        pick_one = input("Pick a Number from 1 to " + str(len(list)) + " > ")
        pick_one = int(pick_one) - 1
        display_list(list[pick_one])
        add_start = [input("Add another fruit. > ")]
        list = add_start + list
        display_list(list)
        insert_start = input("And another... > ")
        list.insert(0, insert_start)
        display_list(list)


        for item in list:
            if item.startswith("P"):
                print(item)

        part_deux(list)

def part_deux(list):
    display_list(list)
    list.pop()
    display_list(list)

    list2 = [item.lower() for item in list]

    remove_fruit = input("pick a fruit to remove from the list. > ")
    remove_fruit = remove_fruit.lower()

    find_it = list2.index(remove_fruit)

    del list[find_it]
    display_list(list)
    part_three(list)

def part_three(list):
    remove_items = []

    for item in list[:]:
        answer = input("Do you like %s? > " % (item.lower()))
        answer = answer.lower()

        while answer != "yes" and answer != "no":
            answer = input("You must answer yes, or no. > ")

        if answer == "no":
            list.remove(item)

    display_list(list)
    part_four(list)

def part_four(list):
    """not sure if i've succeeded in what you're after here or not, but it works as expected based on my
    interpretation of the instructions.
    """

    list_copy = list[:]

    for item in list_copy:
        list_copy[list_copy.index(item)] = item[::-1]
    display_list(list_copy)
    list.pop()
    display_list(list)
    display_list(list_copy)


def display_list(list):
    print(list)


def add_end(list, item):
    list.append(item)
    display_list(list)
    return list

main()
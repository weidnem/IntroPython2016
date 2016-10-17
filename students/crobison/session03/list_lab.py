# Charles Robison
# 2016.10.15
# List Lab

#!/usr/bin/env python3

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
str_length = len(fruits)

print("Here's the current list of fruits: ")
for i in fruits:
    print(i)

# Ask the user for another fruit and add it to the end of the list.
response = input("Please add another to the list: ")
fruits.append(response)
str_length = len(fruits)

print("Here's the updated list of fruits: ")
for i in fruits:
    print(i)

# Ask the user for a number and display the number back to the user
# and the fruit corresponding to that number (on a 1-is-first basis).
response = input("Pick a number from the list of fruits, equal to or less than " + str(str_length) + ":")

print("You picked " + fruits[int(response)-1] +".  Good choice!")

# Add another fruit to the beginning of the list using “+” and display the list.
response = input("Please add another to the list: ")
fruits = [response] + fruits

print("Here's the updated list of fruits: ")
for i in fruits:
    print(i)

# Add another fruit to the beginning of the list using insert()
# and display the list.
response = input("Please add another to the list: ")
fruits.insert(0, response)
print("Here's the updated list of fruits: ")
for i in fruits:
    print(i)

# Display all the fruits that begin with “P”, using a for loop.
print("Here are all the fruits in the list that begin with 'P': ")
for i in fruits:
    if i[0] == 'P':
        print(i)







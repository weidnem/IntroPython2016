#!/usr/bin/env python3

# Comprehensions Lab

'''
Note: this is a bit of a “backwards” exercise – we show you code, you figure out what it does.

As a result, not much to submit – don’t worry about it – you’ll have a chance to use these in other exercises.
'''

# === List comprehensions

feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']

comprehension = [delicacy.capitalize() for delicacy in feast] # list of strings

comprehension[0] # 'Lambs'

comprehension[2] # 'Orangutans'

# === Filtering lists with list comprehensions

feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals',
            'fruit bats']

comp = [delicacy for delicacy in feast if len(delicacy) > 6]

len(feast) # 5

len(comp) # 3

# === Unpacking tuples in list comprehensions

list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]

comprehension = [ skit * number for number, skit in list_of_tuples ]

comprehension[0] # n * string = string repeated; 'lumberjack'

len(comprehension[2]) # 4 * 4 = 16 ('spamspamspamspam')

# === Double list comprehensions

eggs = ['poached egg', 'fried egg']

meats = ['lite spam', 'ham spam', 'fried spam']

comprehension = \
[ '{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]

len(comprehension) # 6 (0 - 5)

comprehension[0] # 'poached egg and lite spam'
comprehension[1] # 'poached egg and ham spam'
comprehension[5] # 'fried egg and fried spam'

# === Set comprehensions

comprehension = { x for x in 'aabbbcccc'} # {} defines dictionary, or set

comprehension # {'a', 'b', 'c'} type = set

# === Dictionary comprehensions

dict_of_weapons = {'first': 'fear',
    'second': 'surprise',
    'third': 'ruthless efficiency',
    'forth': 'fanatical devotion',
    'fifth': None}

dict_comprehension = \
{ k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}

'first' in dict_comprehension # Guess: None Actual: False

'FIRST' in dict_comprehension # True

len(dict_of_weapons) # 5

len(dict_comprehension) # 4

# === Count Even Numbers

'''
This is from CodingBat “count_evens” (http://codingbat.com/prob/p189616)

Using a list comprehension, return the number of even integers in the given array.

Note: the % “mod” operator computes the remainder, e.g. 5 % 2 is 1.

count_evens([2, 1, 2, 3, 4]) == 3

count_evens([2, 2, 0]) == 3

count_evens([1, 3, 5]) == 0

def count_evens(nums):
   one_line_comprehension_here
'''

def count_evens(list_of_numbers):
    result = len([evens for evens in list_of_numbers if evens % 2 == 0])
    return result

# ===

if __name__ == '__main__':
    print('\n=== MAIN ===\n')

print('\ncount_evens([2, 1, 2, 3, 4])')
print(count_evens([2, 1, 2, 3, 4])) # 3

print('\ncount_evens([2, 2, 0])')
print(count_evens([2, 2, 0])) # 3

print('\ncount_evens([1, 3, 5])')
print(count_evens([1, 3, 5])) # 0


'''
1. Print the dict by passing it to a string format method, so that you get 
something like:

“Chris is from Seattle, and he likes chocolate cake, mango fruit,
greek salad, and lasagna pasta”

2. Using a list comprehension, build a dictionary of numbers from zero to 
fifteen and the hexadecimal equivalent (string is fine). (the hex() function 
gives you the hexidecimal representation of a number.)

Do the previous entirely with a dict comprehension – should be a one-liner

4. Using the dictionary from item 1: Make a dictionary using the same keys but 
with the number of ‘a’s in each value. You can do this either by editing the 
dict in place, or making a new one. If you edit in place, make a copy first!

5. Create sets s2, s3 and s4 that contain numbers from zero through twenty, 
divisible 2, 3 and 4.

Do this with one set comprehension for each set.
What if you had a lot more than 3? – Don’t Repeat Yourself (DRY)
create a sequence that holds all three sets
loop through that sequence to build the sets up – so no repeated code.
Extra credit: do it all as a one-liner by nesting a set comprehension inside a 
list comprehension. (OK, that may be getting carried away!)
'''

'''
=== SAMPLE ===

'''
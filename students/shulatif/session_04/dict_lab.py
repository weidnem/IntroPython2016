#!/usr/bin/env python3

person = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

print(person)

# Remove the cake entry
person.pop('cake')

print(person)

# add entry for fruit
person['fruit'] = 'Mango'

print(person)

# Display just the keys
print(person.keys())

# Display just the values
print(person.values())

# Is cake a key?
if 'cake' in person:
    print('True')
else: print('False')

# Is mango a value?
if 'Mango' in person.values():
    print('True')
else: print('False')

# Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value.
weird_dict = person.copy()
for value in person:
    weird_dict[value] = person[value.lower()].count('t')
print(weird_dict)

# Creating s1 so to make the other sets
s1 = set(range(0, 21))

def create_sets(str, div):
    """
    To create new sets divisible by whatever number based off set s1.
    For some reason this did not work.
    :param str: name of the set to create
    :param div: number to be divisible by
    :return: a new set with just those numbers
    """
    str = set()
    for i in s1:
        if i % div == 0:
            print('adding {}'.format(i))
            print(str)
            return str.add(i)
        else: pass

# create_sets('s2', 2)
# create_sets('s3', 3)
# create_sets('s4', 4)

# For set s2, all the numbers divisible by 2 from s1
s2 = set()
for i in s1:
    if i % 2 == 0:
        s2.add(i)
print('s2 {}'.format(s2))

# For set s3, all the numbers divisible by 3 from s1
s3 = set()
for i in s1:
    if i % 3 == 0:
        s3.add(i)
print('s3 {}'.format(s3))

# For set s4, all the numbers divisible by 4 from s1
s4 = set()
for i in s1:
    if i % 4 == 0:
        s4.add(i)
print('s4 {}'.format(s4))

print(s3.issubset(s2))
print(s4.issubset(s2))

pyset = set('Python')
pyset.add('i')
marathon = frozenset('marathon')
print(pyset.intersection(marathon))
print(pyset.union(marathon))


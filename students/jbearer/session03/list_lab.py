#!/usr/bin/env python3
"""
List Lab -- October 12, 2016
"""

def fruit_tree():
    print('-> List Lab: Section 1 <-')
    l = ['Apples', 'Pears', 'Oranges', 'Peaches' ]
    print("Original list:", l)
    
    add_fruit = input('What fruit would you like to add? ')
    l.append(add_fruit)
    print('List with input:', l)
    
    l_size = len(l)
    pick_fruit = int(input('Pick a number between 1 and %d: ' % l_size ))
    print('You picked fruit: %s' % l[pick_fruit - 1])
    
    l = ['Pinapple'] + l
    print('List add with + operator', l)
    
    l.insert(0, 'Strawberry')
    print('List add with .insert()', l)
    
    for fruit in l:
        if fruit[0] == 'P':
            print('Starts with "P": %s' % fruit)
    
    print()
    print('-> List Lab: Section 2 <-')
    print('Starting list:', l)

    l.pop()
    print('Last fruit removed:', l)

    del_fruit = input('Which fruit would you like to delete? ')
    l.pop(l.index(del_fruit))
    print('Current list:', l)


fruit_tree()

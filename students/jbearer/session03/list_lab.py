#!/usr/bin/env python3

def fruit_tree():
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

fruit_tree()

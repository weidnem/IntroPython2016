#!/usr/bin/env python3

'''
Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”.
Display the dictionary.
Delete the entry for “cake”.
Display the dictionary.
Add an entry for “fruit” with “Mango” and display the dictionary.
Display the dictionary keys.
Display the dictionary values.
Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
Display whether or not “Mango” is a value in the dictionary (i.e. True).
'''

d = {'name' : 'Chris', 'city' : 'Seattle', 'cake' : 'chocolate'}

# d.keys()
# dict_keys(['score', 'name'])
# 
# d.values()
# dict_values([42, 'Brian'])
# 
# d.items()
# dict_items([('score', 42), ('name', 'Brian')])

if __name__ == "__main__":
    print('\nDisplay the dictionary.')
    print(d)
    
    print('\nDelete the entry for “cake”.')
    d.pop('cake')
    
    print('\nDisplay the dictionary.')
    print(d)
    
    print('\nAdd an entry for “fruit” with “Mango” and display the dictionary.')
    d['fruit'] = "Mango"
    print(d)
    
    print('\nDisplay the dictionary keys.')
    print(d.keys())
    
    print('\nDisplay the dictionary values.')
    print(d.values())
    
    print('\nDisplay whether or not “cake” is a key in the dictionary (i.e. False) (now).')
    print("'cake' in d =", 'cake' in d)
    
    print('\nDisplay whether or not “Mango” is a value in the dictionary (i.e. True).')
    print("'Mango' in d.values() =", "Mango" in d.values())
    



    
    
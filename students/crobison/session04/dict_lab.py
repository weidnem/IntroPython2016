# Charles Robison
# 2016.10.18
# Dictionary and Set Lab

# Create a dictionary containing “name”, “city”, and “cake”
# for “Chris” from “Seattle” who likes “Chocolate”.
d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

#Display the dictionary.
d

# Delete the entry for “cake”.
del d['cake']

# Display the dictionary.
d

# Add an entry for “fruit” with “Mango” and display the dictionary.
d['fruit'] = 'Mango'
d

# Display the dictionary keys.
d.keys()

# Display the dictionary values.
d.values()

# Display whether or not “cake” is a key in the dictionary
# (i.e. False) (now).
'cake' in d

# Display whether or not “Mango” is a value in the dictionary
#  (i.e. True).
'Mango' in d.values()

# Using the dictionary from item 1: Make a dictionary using
# the same keys but with the number of ‘t’s in each value.
d = {'name': 0, 'city': 2, 'cake': 1}


# Create sets s2, s3 and s4 that contain numbers from zero through
# twenty, divisible 2, 3 and 4.
s2 = set(i for i in range(0,21) if i % 2 == 0)
s3 = set(i for i in range(0,21) if i % 3 == 0)
s4 = set(i for i in range(0,21) if i % 4 == 0)

# Display the sets.
s2
s3
s4

# Display if s3 is a subset of s2 (False)
# and if s4 is a subset of s2 (True).
s3.issubset(s2)
s4.issubset(s2)

# Create a set with the letters in ‘Python’ and add ‘i’ to the set.
x = 'Python'
setp = set(i for i in x)
setp.add('i')

# Create a frozenset with the letters in ‘marathon’
y = 'marathon'
setm = frozenset(i for i in y)

# display the union and intersection of the two sets.
setu = setp|setm
setu
seti = [setp, setm]
set.intersection(*seti)









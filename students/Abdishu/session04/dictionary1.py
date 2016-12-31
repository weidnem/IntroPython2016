 		
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
Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value.
Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
Display the sets.
Display if s3 is a subset of s2 (False)
and if s4 is a subset of s2 (True).
Create a set with the letters in ‘Python’ and add ‘i’ to the set.
Create a frozenset with the letters in ‘marathon’
display the union and intersection of the two sets.

'''

dict1 = {'Name':'Chris', 'City':'Seattle','cake':'Chocalate'}
print(dict1)

dict1.pop('cake')

print(dict1)

dict1['fruit'] = 'Mango'

print(dict1)

dict1.keys()
dict1.values()
if 'cake' in dict1:
    print("Cake is in dictionary key")
else:
    print("Cake is not in dictionary key")

def Is_manago():

	for i in dict1.values():
		if i.lower() == 'mango':
			return "Manago  is in dictionary"
	

print(Is_manago()) 

#CREATING SET S2,3, AND 4 

s2 = {i for i in range(0,21) if i%2==0}

s3 = {j for j in range(0,21) if j%3==0}

s4 = {i for i in range(0,21) if i%2==0}
#DISPLAYING SET
print(s2)
print()
print(s3)
print()
print(s4)

# Display if s3 is a subset of s2 (False)
print(s3.issubset(s2)) 

#and if s4 is a subset of s2 (True).
print(s4.issubset(s2)) 

#Create a set with the letters in ‘Python’ and add ‘i’ to the set.

string ="Python"
s = set(string)
print(s)
s.add('i') 
print(s)

#Create a frozenset with the letters in ‘marathon’

frozen_set = frozenset("marathon")
print(frozen_set)

#display the union and intersection of the two sets.

print("The intersection of the two set is:  ", s.intersection(frozen_set))
print("The union of the two set is:  ", s.union(frozen_set))

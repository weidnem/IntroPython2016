dict1 = {'Name':'Chris', 'City':'Seattle','cake':'Chocalate'}
print(dict1)

dict1.pop('cake')

print(dict1)

dict1['fruit'] = 'Mango'

print(dict1)

dict1.keys()
dict1.values()
'cake' in dict1

def Is_manago():

	for i in dict1.values():
		if i.lower() == 'mango':
			return "Manago  is in dictionary"
	

print(Is_manago()) 		

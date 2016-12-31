'''
Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
Display the list.
Ask the user for another fruit and add it to the end of the list.
Display the list.
Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).
Add another fruit to the beginning of the list using “+” and display the list.
Add another fruit to the beginning of the list using insert() and display the list.
Display all the fruits that begin with “P”, using a for loop.
'''
li = ["Apples", "Pears", "Oranges", "Peaches"]

print(li)

anofruit= input('Please enter another furit:-  ')

li.append(anofruit)

print(li)

number = int(input("Enter a number from 0 to 4:-  "))

print("You have entered", number , "The fruit corresponding to that number is", li[number] )

li.insert(0,'Banana')

print(li)

for frt in li:
        if frt[0].lower()=='p':
                print(frt," Begins with ->P")

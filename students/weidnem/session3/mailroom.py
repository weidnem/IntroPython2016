# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 20:19:38 2016

@author: noner_000
"""


userin = ''
donors = {"rick doe": [34,45],"jake doe": [12,55],"pat doe": [1324,1],"jane doe": [5750,1331],"sally doe": [3,2]}

def amount_entry(don_list):
    amt = ''
    while type(amt) is str:
        amt = input("enter amount--> ")
        if 

def donor_entry():
    action = 0
    while action == 0:
        userin = input("Enter donor's full name--> ")
        
        if userin == 'list':
            for i in donors:
                print(i)
            action = 0
        elif userin in donors:
            amount_entry(userin)
            action = 1
        elif userin not in donors:
            donors.update({userin:[]})
            action = 1
        else:
            action = 0
        
        donors.update({userin:amount_entry(donors[userin]}))
            
            
    
#    If the user types ‘list’, show them a list of the donor names and re-prompt
#If the user types a name not in the list, add that name to the data structure and use it.
#If the user types a name in the list, use it.
#Once a name has been selected, prompt for a donation amount.
#Verify that the amount is in fact a number, and re-prompt if it isn’t.
#Once an amount has been given, add that amount to the donation history of the selected user.
#Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.



if __name__ == '__main__':
    print("Welcome to the Mailroom!")
    while userin != "q":
        print("Enter a Command")
        print("    1 = Send a Thank You")
        print("    2 = Create a Report")
        userin = input("--> ")
        if userin == 1:
            donor_entry()
        elif userin == 2:
            donor_report()
        else:
            print("invalid entry...)

            
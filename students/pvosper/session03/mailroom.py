#!/usr/bin/env python3

print("You've Got Mail!")

donor_list = [
    ["Domingo Nair", [75, 50, 25]],
    ["Cruz Woodman", [100]],
    ["Quinn Halvorsen", [125, 500, 50]],
    ["Carlota Lamkin", [50, 200]],
    ["Angelyn Meekins", [500, 50]],
    ["Maryland Cassel", [100, 50, 60]],
    ["Muoi Macken", [125]],
    ["Robby Remus", [25, 50, 75]],
    ["Arlette Vanderveer", [125, 50]],
    ["Reed Brantley", [125, 50, 200]],
    ["Lenard Hardegree", [100]],
    ["Lashunda Mckeithan", [125, 50]],
    ["Eveline Paquette", [100, 250]],
    ["Shawana Cano", [125, 50, 250]],
    ["Phylicia Sansbury", [25, 100]],
    ["Ricarda Wykoff", [100, 50, 200]],
    ["Lue Mollett", [125, 50, 250]],
    ["Janean Hetzler", [125, 50]],
    ["Garth Figura", [125]],
    ["Kurt Cowherd", [100, 50, 25]]
    ]

def donor_total(index):
    donations = 0
    for entry in donor_list[index][1]:
        donations += entry
    return donations
    
def list_donors():
    for entry in donor_list:
        print(donor_list[entry][0])
        
def find_donor(str):
    for entry in donor_list:
        check = entry[0].lower()
        if check.find(str.lower()) > -1:
            return donor_list[donor_list.index(entry)]
    return

def second_element(list):
    return list[1]

def report_donors():
    temp_list = []
    for i in range(len(donor_list)):
        entry_donation_total = donor_total(i)
        temp_list.append([donor_list[i][0], entry_donation_total])
    temp_list = sorted(temp_list, key=second_element, reverse=True)
    for donor in temp_list:
        print(donor[0], "\t$", donor[1]) # $todo: better string formatting

start_message = ('''
Choose from one of the following actions:
    m   Mail a Thank You letter to a selected donor
    r   Report list of all donors, sorted by donation size
    x   Exit the program
''')

def mailroom_script():

    while True:

        print(start_message)
    
        response = input().strip().lower()
    
        if response == "m":
            print("list")
        
        elif response == "r":
            print("Report of all donors, sorted by donation size:")
            report_donors()

        elif response == "x":
            break
    
        else:
            print("try again")
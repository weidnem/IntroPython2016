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
        check = entry[0]
        print(check.find(str))
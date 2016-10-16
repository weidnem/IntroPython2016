#!/usr/bin/env python3

print("You've Got Mail!")

# ===== Initial data set =====

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

# ===== Utilities =====

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
    return False

def second_element(list):
    return list[1]

# ===== Main Elements =====

start_message = ('''
Choose from one of the following actions:
    m   Mail a Thank You letter to a selected donor
    r   Report list of all donors, sorted by donation size
    x   Exit the program
''')

def mail_message(donor_info):
    donations = 0
    for entry in donor_info[1]:
        donations += entry
    first_name = donor_info[0][:donor_info[0].index(' ')]
    form = '''\
    Dear {name},
    Thank you so much for your generous donation of ${amount:0.2f}.
    Without such selfless contributions from people like you, we
    would not be able to continue this important work.
    We are all very appreciative of your support!
    
    Sincerely,
    
    Carl
    '''
    print(form.format(name=first_name, amount=donations))

def mail_thank_you():
    target_donor = []
    print('''
    First you'll need to select a donor to mail.
    Enter a full or partial name to search for:
    ''')
    response = input().strip().lower()
    target_donor = find_donor(response)
    if target_donor != False:
        print("Mail to:", target_donor[0])
        print("Is this correct? (y/n)")
        correct_response = input().strip().lower()
        if correct_response == "y":
            print(mail_message(target_donor))
            return
    else:
        print("Sorry, but {} could not be found".format(response))
        return
    
def report_donors():
    temp_list = []
    for i in range(len(donor_list)):
        temp_list.append([donor_list[i][0], donor_total(i)])
    temp_list = sorted(temp_list, key=second_element, reverse=True)
    for donor in temp_list:
        print(donor[0], "\t$", donor[1]) # $todo: better string formatting

def main():

    while True:

        print(start_message)
    
        response = input().strip().lower()
    
        if response == "m":
            print("This will allow you to pick a donor, then send a Thank You message")
            mail_thank_you()
        
        elif response == "r":
            print("Report of all donors, sorted by donation size:")
            report_donors()

        elif response == "x":
            print("Exiting program")
            break
    
        else:
            print("try again")
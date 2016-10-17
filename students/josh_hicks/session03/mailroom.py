#!/usr/bin/env python

donor_list = {'Bill Clinton': [100, 200, 300], 'Hilary Clinton': [200, 400],
              'Chelsea Clinton': [50], 'Barrack Obama': [250, 350, 450],
              'Michele Obama': [100, 300]}


def main():
    while True:
        display_menu()
        selection = input("->")
        if selection == "1":
            do_thankyou()
        elif selection == "2":
            do_report()
        else:
            pass


def display_menu():
    print("Choose an action:")
    print(" 1. Send a Thank You")
    print(" 2. Create a Report")


def do_thankyou():
    print("Enter donor's full name (type 'list' for donor list)")
    donor_name = input("->")
    if donor_name == "list":
        show_donorlist()
    else:
        while True:
            donation_amount = input("Enter donation amount:")
            try:
                donation_amount = int(donation_amount)
                break
            except Exception as e:
                print("Invalid input")
        add_donation(donor_name, donation_amount)


def show_donorlist():
    print("Donor List:")
    for donor, contributions in donor_list.items():
        joined_contributions = ','.join(map(str, contributions))
        print("{0}: {1}".format(donor, joined_contributions))
    print()


def add_donation(donor, amount):
    try:
        contribution_list = donor_list[donor]
        contribution_list.append(amount)
        print("Donation recorded successfully!")
        print("{0}: {1}".format(donor, ','.join(map(str, contribution_list))))
        print()
    except Exception as e:
        print("Donor not found")


if __name__ == '__main__':
    main()

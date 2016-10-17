# !/usr/bin/env python3

"""
Name: Paul Briant
Date: 10/18/16
Class: Introduction to Python
Session: 03
Assignment: Mailroom

Description:

"""
# -------------------------------Functions--------------------------------------


def print_report(donors):
    """

    """



def send_ty(donors):
    """

    """
    full_name = input("Please enter your full name: ")
    if full_name == 'list':
        for item in donors:
            print(item[0])
        full_name = input("Please enter your full name: ")
    if full_name not in donors:
        # Add new donor name to donors
        donors.append([full_name, []])
    # Prompt for a donation amount
    amount = input("How much would you like to donate? ")
    # Verify amount is a number
    if not amount.isnumeric():
        amount = input("How much would you like to donate? ")
    # Append to donor in donors
    donors[full_name].append(amount)
    # Display thank you
    print("""
    Dear {},
    Thank you for your generous donation of ${d:}!
    Your contribution to this organization will greatly
    impact our efforts to complete our mission.
    """).format(donors[full_name[0]], donors[full_name[-1]])


def add_donor(name, donors, amount):
    """

    """
    for item in donors:
        if name == item[0]:
            item[1].append(amount)
    return donors

# ==============================================================================


def main():
    """

    """
    donors = [['Bill Gates', [1000000, 2500000, 1800000]],
              ['Sheryl Sandberg', [200000, 100000, 130000]],
              ['Larry Page', [150000, 110000, 170000]],
              ['Satya Nadella', [140000, 111000]],
              ['Susan Wojcicki', [100000, 109000]]]

    message = """
    Please select from the following options:

    To send a thank you: type "s"
    To print a report: type "p"
    To exit: type "x"
    """

    action = ''
    # Continue to prompt user until user enters 'x'
    while True:
        # Provide options and prompt the user for a response.
        print(message)
        # Remove any additional white space.
        action = input('==> ').strip()
        # Determine action to take.
        if action == 's':
            send_ty(donors)
        elif action == 'p':
            print_report(donors)
        elif action == 'x':
            break
        else:
            print('please type "s", "p", or "x"')


if __name__ == '__main__':
    main()

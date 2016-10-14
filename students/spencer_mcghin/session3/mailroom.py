#!/usr/bin/env python3

"""List of Donors and Amounts Donated"""

donors = ["Nick Padgett", "Julia Allen", "Pete Tamisin", "Charles Elliott", "Andy Rocha", "Beth DeSousa"]
Nick = [12312, 34230, 38593]
Julia = [49203, 5023, 9052]
Pete = [9503, 2093, 10932, 40923]
Charles = [209, 50912, 9026]
Andy = [20968, 2091, 8934]
Beth = [29092, 5906, 8734]

"""Function to generate thank you letter to a selected donor"""

def thank_you():
donor = input("Please enter the name of a donor, or type 'list' in order to display a list of donors." '\n'
"> ")





"""Function to generate a report of donors sorted by total amounts donated"""

def print_donor_list():


"""Prompt user for input to generate thank you letter or report and validate selection"""

print("Hi there. What would you like to do?" '\n'
      "Generate a thank you letter (1)" '\n'
      "Generate a donor report (2)")
action = input("> ")
while action != 1 or 2:
    action = input("> ")
if action == 1:
    thank_you()
else:
    print_donor_list()


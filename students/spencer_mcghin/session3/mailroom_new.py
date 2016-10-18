#!/usr/bin/env python3

import numpy


"""Dictionary of Donors and Amounts Donated"""

donors = {"Nick Padgett": [12312, 34230, 38593],
          "Julia Allen": [49203, 5023, 9052],
          "Pete Tamisin": [9503, 2093, 10932, 40923],
          "Charles Elliott": [209, 50912, 9026],
          "Andy Rocha": [20968, 2091, 8934],
          "Beth DeSousa": [29092, 5906, 8734]}


""" Input variables """

# Input for thank you, add user, or report #

user_input = input("Hey there! Please select one of the following options or type 'list' to see the current donor list '\n'"
                   "1.) Send A Thank You Letter '\n'"
                   "2.) Generate a Donor Report '\n"
                   "> ")

# Input for donation amount #

donation_amount = input("Please enter a donation amount '\n'"
                        "> ")


"""

Functions for program

"""

"""Send a thank you functions"""

# Print donor list #

def print_donor_list():
    for donor, donation in donors.items():
        print(donor)

# Add donor name to list #

def add_donor():
    donors.update(user_input)

# Add donation amount to new donor #

def add_amount():
    donors.update({user_input : donation_amount})

# Verify donation amount is an integer #

def check_donation():
    while isinstance(donation_amount, int):
        add_amount()
    else:


# Print email to terminal #


def print_email():
        print("Hello %r, Thank you so much for your generous donation to our very charitable organization." '\n'
              "Your contribution will help us to further our reach in providing charitable services to those in need." '\n'
              "We hope that you will continue to support our organization in the future." '\n'
              "Sincerely," '\n'
              '\n'
              "Spencer McGhin")


"""Print donor donation report functions"""


def print_report():


# Print total donor donations #

def print_donation_total():
    for donor, donations in sorted(donors.items()):
        print(sum(donations))

# Print total number of donations #

def print_num_donations():
    for donor, donations in sorted(donors.items()):
        print(len(donations))

# Print average donation #

def print_avg_donation():
    for donor, donations in sorted(donors.items()):
        print(int(numpy.mean(donations)))


# Output info for tabulate format #
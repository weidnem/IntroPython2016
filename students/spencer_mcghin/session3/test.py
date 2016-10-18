import numpy

"""Dictionary of Donors and Amounts Donated"""

donors = {"Nick Padgett": [12312, 34230, 38593],
          "Julia Allen": [49203, 5023, 9052],
          "Pete Tamisin": [9503, 2093, 10932, 40923],
          "Charles Elliott": [209, 50912, 9026],
          "Andy Rocha": [20968, 2091, 8934],
          "Beth DeSousa": [29092, 5906, 8734]}


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


def test():
    for donor in donors:
        print([print_donation_total(), print_num_donations(), print_avg_donation()])




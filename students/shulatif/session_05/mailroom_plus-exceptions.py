donor_list = [
    {'first': 'Hilary', 'last': 'Clinton', 'donations': [100, 30, 10]},
    {'first': 'Bernie', 'last': 'Sanders', 'donations': [20, 40]},
    {'first': 'Shu', 'last': 'Latif', 'donations': [10000]},
    {'first': 'God', 'last': '', 'donations': [10000]},
    {'first': 'Steve', 'last': 'Jobs', 'donations': [90, 80, 20]}
               ]


def write_letter(filename, letter):
    file = open(filename, 'w+')
    file.writelines(letter)
    file.close()


def printdonors():
    """
    This will just print out the donors and the total amount they have donated. The space variable is just taking the
    total length of donor and donation amount and adding the right amount of spaces to add a '#' evenly for a box.
    :return: Boxed list of donors and total donor amounts.
    """
    print('#==========================#')
    for donor in donor_list:
        donation = sum(donor['donations'])
        space = " " * (19 - (len(donor['first']) + len(donor['last']) + len(str(donation))))
        print('# {first} {last} - ${donation} {space}#'.format(**donor, donation=donation, space=space))
    print('#==========================#')


def thankyou():
    """
    :param donor: Donor Name
    :param donation: Donation Total
    :return: Prints out a thank you email to each donor.
    """
    for donor in donor_list:
        print('Writing thank you note to {} {}.'.format(donor['first'], donor['last']))
        donation = sum(donor['donations'])
        letter = '''
        Dear {0} {1},
        Thank you for your donation of ${2} to the Coalition of Never Selecting Evil Neanderthal Trump! Together we can make sure our
        country does not succumb to hate and fear. Your money will go towards helping to educate the masses and expose
        Donald Trump for the fraud and opportunist that he is.
        '''.format(donor['first'], donor['last'], donation)
        filename = '{}_{}'.format(donor['first'], donor['last'])
        print('\033[1m' + '\033[93m' + 'Wrote to file: {}'.format(filename) + '\033[0m')
        write_letter(filename, letter)


def finddonor(donor_name):
    """
    To match donor name.
    :param donor_name:
    :return:
    """
### THIS IS BROKEN ###
    for donor in donor_list:
        if donor_name == donor['first'] + ' ' + donor['last']:
            return donor
        else:
            return None


def creatreport():
    """
    This will print the donor, total amount donated, number of donations, and average amount of donations.
    :return: donor, total, number of donations, average donations in a nice table.
    """
    print('{:25s}  |  {:11s} | {:9s} | {:12s}'.format('Donor Name', 'Total Donated', 'Number of Donations', 'Average Donations\n'))
    for donor in donor_list:
        avg = round(sum(donor['donations']) / len(donor['donations']))
        total = sum(donor['donations'])
        don_amt = len(donor['donations'])
        name = donor['first'] + ' ' + donor['last']
        print('{:25s} {:16.2f} {:15d} {:25.2f}'.format(name, total, don_amt, avg))


def start():
    """
    This is the main menu where they can list the donors and total donated, add new donors, print thank you notes
    or create a report. We do not allow floating numbers for donation because people who donate fractional dollars
    are stupid and we don't have stupid donating to this foundation.
    :return:
    """
    ty_input = ''
    while ty_input != 'q':
        ty_input = input('''
#======================================================#
# Please make a selection from the following choices:  #
#                                                      #
# list - List donors and totals                        #
# add - Add a new donor or donation                    #
# 1 - Send a Thank You Note                            #
# 2 - Create Report                                    #
# q : To Quit                                          #
#======================================================#
        ''')
        if ty_input.lower() == 'q':
            print('Goodbye!')
            break
        elif ty_input.lower() == 'list':
            printdonors()
            print('\n')
        elif ty_input.lower() == 'add':
            donor_fname = input('Donor First Name: ')
            donor_lname = input('Donor Last Name: ')
            donor_name = {'first': donor_fname, 'last': donor_lname}
            donor = finddonor(donor_name)
            if donor is None:
                amount = int(input('Enter donation amount $ '))
                donor_name.update(donations=[amount])
                donor_list.append(donor_name)
            else:
                amount = int(input('Enter donation amount $ '))
                donor.update(donations=[amount])
        elif ty_input == '1':
            thankyou()
        elif ty_input == '2':
            creatreport()
        else:
            print('\033[1m' + '\033[93m' + 'I did not understand. Please try again.' + '\033[0m')

if __name__ == '__main__':
    start()

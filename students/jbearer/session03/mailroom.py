#!/usr/bin/env python3
"""
Excercise --  Mailroom
October 14, 2016
"""

donor_list = {'Shrek':[5,10], 'Donkey':[23,101,4], 'Princess Fiona':[7,28],
'Puss in Boots':[36,12,10], 'Gingerbread Man':[12,34]}

def print_report():
    print('### Donor Report ###')
    print('{:16} {:6} {:6}'.format('Name','Total','Donations'))
    sort_l = []
    for name, donations in donor_list.items():
        sort_l.append((name, sum(donations), len(donations)))
    
    sort_l = sorted(sort_l, key=lambda donations: donations[1], reverse=True)
    for i in sort_l:
        print('{:15} {:6} {:6}'.format(i[0],i[1],i[2]))

def proc_donation(d_name):
    amt = ''
    while amt == True:
        try:
            donation = int(input('Enter donation amount: '))
        except ValueError:
            continue
        else:
            if d_name in donor_list:
                donor_list[d_name].append(donation)
            elif d_name not in donor_list:
                donor_list[name] = [donation]
            amt = False
        return donation



def send_thanks():
    chk = True
    amt = True
    while chk == True:
        name = input('Enter name or type "list": ')
        if name == 'list':
            for d_names in donor_list.keys():
                print(d_names)
        # elif name in donor_list or name not in donor_list:
        #     proc_donation(name)
        #     chk = False
        elif name in donor_list:
            while amt == True:
                try:
                    donation = int(input('Enter donation amount: '))
                except ValueError:
                    continue
                else:
                    donor_list[name].append(donation)
                    amt = False
                    chk = False
        elif name not in donor_list:
            while amt == True:
                try:
                    donation = int(input('Enter donation amount: '))
                except ValueError:
                    continue
                else:
                    donor_list[name] = [donation]
                    amt = False
                    chk = False
    print('Thank you {} for your donation of ${}.'.format(name,donation))

# here is where triple quoted strings can be helpful
msg = """
What would you like to do?
To send a thank you: type "s"
To print a report: type "p"
To exit: type "x"
"""


def main():
    """
    run the main interactive loop
    """

    response = ''
    # keep asking until the users responds with an 'x'
    while True:  # make sure there is a break if you have infinite loop!
        print(msg)
        response = input("==> ").strip()  # strip() in case there are any spaces

        if response == 'p':
            print_report()
        elif response == 's':
            send_thanks()
        elif response == 'x':
            break
        else:
            print('please type "s", "p", or "x"')

if __name__ == "__main__":
    main()
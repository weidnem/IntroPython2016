from prettytable import PrettyTable


def people(totes, **kwargs):
    """
    Here we deal with how many people will be in the league and how many people should be getting a payout. Then
    we can deal with what percentage of the payout they will get.
    :param totes: Total number of people in the league.
    :param kwargs: How many people should get a payout, of those, what is the percentage breakdown of them. We
    will make this a set.
    :return: This will return a dictionary to be used in later functions
    """
    # TO DO
    pass


def fantasy_math(*args, **kwargs):
    """
    This does the math for the fantasy pool and coverts back to a string with the $ in it.
    :param args: this should be a tuple of percentages for the payout.
    :param kwargs: This is included for future use to scale the payout for more than 3 people. TO DO.
    :return: Will return a tuple of strings of payouts with the $ included.
    """
    total = [payout * pool / 100 for payout in args]
    firstpay, secondpay, thirdpay = ['${}'.format(each) for each in total]
    return firstpay, secondpay, thirdpay


def convert_perc(*args):
    """
    Will convert the percentage to strings to include the percentage sign in our print out.
    :param args: a tuple of the percentages
    :return: Tuple of strings with % at the end.
    """
    percs = args
    firstplace, secondplace, thirdplace = ['{}%'.format(each) for each in percs]
    return firstplace, secondplace, thirdplace


while True:
    try:
        print('Welcome to the fantasy football payout calculator! To begin we need to get some information.')
        totes = int(input('How many people will be in your league?: '))
        buyin = float(input('What is the buy in cost? $: '))
        #payees = input('How many people will be paid out?: ')
        pool = totes * buyin
        print('Your total pot will be ${}'.format(pool))
        firstplace = float(input('What percentage of the pot will first place get? %: '))
        secondplace = float(input('What percentage of the pot will second place get? %: '))
        thirdplace = float(input('What percentage of the pot will third place get? %: '))
        first, second, third = fantasy_math(firstplace, secondplace, thirdplace)
        firstplace, secondplace, thirdplace = convert_perc(firstplace, secondplace, thirdplace)
        print('For your league the payout will be as follows:')
        pt = PrettyTable(['Rank', 'Percentage', 'Payout'])
        pt.align = 'r'
        pt.add_row(['First place', firstplace, first])
        pt.add_row(['Second place', secondplace, second])
        pt.add_row(['Third place', thirdplace, third])
        print(pt)
        break
    except ValueError as e:
        print('\033[1m' + '\033[93m'+'You have entered an invalid input. Total number of people can only be integers,\
other inputs can be floating numbers. Here is the error that occured: \033[0m \n{}'.format(e))



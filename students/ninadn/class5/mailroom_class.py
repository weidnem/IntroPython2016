'''Mailroom.py using classes for the various donors'''

class donor_info(object):
	"""This class helps us store the name and donation information for each donor. Previously,
	we did so by using a complicated list, tuple, list combination (I also tried dictionaries
	to no avail. By using classes, we can simplify this process greatly, especially since we
	will store similar information for each donor. Specifically, I want to use lists within
	classes and am interested to see how that works."""
	_registry = []
	num_of_donors = 0	#defining the number of donors

	def __init__(self, first, last, donations):
		self._registry.append(self)
		self.first = first
		self.last = last
		self.donations = donations
		donor_info.num_of_donors += 1

'''Donor Database'''
donor1 = donor_info('William', 'Gates', [10000,120000,250000])
donor2 = donor_info('Jeffery', 'Bezos', [20000])
donor3 = donor_info('Paul', 'Allen', [200000, 450000, 1000000])

def print_donors():
	for d in donor._registry:
		print ('{} {}'.format(d.first, d.last))

def create_report():
	pass

def thank_you_note():
	while True:
		name = input ('''Enter a donor's name or 
			type List to see a list of donors or
			type Menu to return to main menu

			Enter your choice: ''').strip()
		if name == "list" or name == "List" or name == "LIST":
			print_donors()
		elif name == "Menu" or name == "menu" or name == "MENU":
			return
		else:
			break

	while True:
		amount_str = input ("Enter an amount (or tpye 'menu' to exit)").strip()
		if amount_str == 'menu' or amount_str = "MENU" or amount_str == "Menu":
			return
		amount = float(amount_str)
		if math.isnan(amount) or math.isinf(amount):
			print ("Invalid amount\n")
			return
		else:
			break


def main_menu_selection():
'''This text is generally a duplicate of the text in the main function. That said, there is some
value to breaking stuff up like this. We could manipulate the while method in the main function
without impacting this specific loop.'''

	action = input('''Enter your selection
		T  Send Thank you note
		R  Create report
		Q  Exit

		Selection: ''')
	return action.strip()

if __name__ == '__main__':
'''It is interesting in this solution, to get user options in the main function. I had previously 
used the main function only to invoke a separare user input function, but that was redundant. While 
it is not good style to pile on all the code in a few functions, all logical code should stay within
a function; no need to break stuff down into too many functions or classes either.'''

	print('''What would you like to do?
		To send a Thank You note, enter T
		To create a report, enter R
		To exit, enter Q\n''')
	running = True
	while running:
		selection = main_menu_selection()
		if selection == 'T' or selection == 't':
			thank_you_note()
		elif selection == 'R' or selection == 'r':
			create_report()
		elif selection == 'Q' or selection == 'q':
			running = False
		else:
			print ('Your selection is invalid')


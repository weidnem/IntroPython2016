#Mailroom assignment from Session 3. 
import sys

def donor_list(tydonorlookup, tydonoramount):
	donordict = {"Bill Gates":[234.34, 23423.44, 23561003.22, 10000000], "Jeffery Bezos": [359400],"Paul Allen": [10000, 200300, 400000.00]}
	if tydonoramount and tydonorlookup:
		donordict[tydonorlookup].append(tydonoramount) 
	totalgiven = []
	averagegiven = []
	donorlist = []
	numbgiven = []
	for key, val in donordict.items():
		donorlist.append(key)
		sum = int(0)
		for i in val:
			sum += int(i)
		totalgiven.append(sum)
		numbgiven.append(len(val))
		averagegiven.append(sum/len(val))
	result = [donordict, donorlist, totalgiven, numbgiven, averagegiven]
	return result

def printdonorlist():
	donorlistprint = donor_list(0,0)
	print ("\n")
	for i, item in zip (range(len(donorlistprint[0])),donorlistprint[0]):
		print (i+1, item)
	print ("\n")

def printdonations():
	printdict = donor_list(0,0)
	#print (printdict)
	dn =  printdict[1]
	tg =  printdict[2]
	ng =  printdict[3]
	ag =  printdict[4]
	print ("| {:20}|  {:20}|  {:20}|  {:20}|".format('Donor Name','Total Given', 'Num Given','Avg. Gift'))
	us = "_"*90
	print (us)
	for i, j, k, l in zip (dn, tg, ng, ag):
		print ("| {:20}|  {:20}|  {:20}|  {:20}|".format(i, j, k, l))
	#for i,j,k,l in printdict[1], printdict[2], printdict[3], printdict[4]:
	#	print ("| {:20}|  {:20}|  {:20}|  {:20}|".format(i, j, k ,l))


def tydonorlook(tydonorselect): 
#This can be done using the enumerate function too
	tydonordict = {}
	donorlist1 = donor_list(0,0)
	lengthrange = range (1, len(donorlist1)+1)
	for i, item in zip(lengthrange,donorlist1):
		tydonordict[i] = item
	print (tydonordict)
	return donorlist1[tydonorselect]

def tyletterprint(tydonorlastname, tydonoramount):
	#tydonorloc = int(tydonorselect)-1
	#print (tydonorloc)
	#donorlist = donor_list()
	#donor = donorlist[tydonorloc]
	#print (donor)
	#donorlastname = donor.split()[1]
	print ('''\n\nDear Mr. {}\n
Thank you very much for your donation of {}.
We have updated our records to reflect your generous donation.

		Thank you,
		The Fund\n'''.format(tydonorlastname, tydonoramount))
	us = "_ _"*25
	print (us)
	print ("\n\n")
	print ('What would you like to do next? \n')
	print ('''Choose an option below: 
	1. Press M to return to main menu
	2. Press any other key to quit\n''')
	tylaction = input("Enter your choice: ")
	if tylaction == 'M' or 'm':
		userinput()
	else:
		sys.exit()
	#printdonations()

def createreport():
	printdonations()
	print ('What would you like to do next? \n')
	print ('''Choose an option below: 
	1. Press M to return to main menu
	2. Press any other key to quit\n''')
	craction = input("Enter your choice: ")
	if craction == 'M' or 'm':
		userinput()
	else:
		sys.exit()


def thankyounote():
	print ('''\nWhom would you like to send the thank you note to?\n
	Enter 1 to see a list of donors to choose from
	Enter 2 to add a new donor
	Enter any other key to go back to the main menu\n''')
	tyaction = input ("Enter Your Choice: ")
	if tyaction == "1":
		printdonorlist()
		tydonorfullname = input ("Enter donor name: ")
		tydonoramount = input ("Enter amount donated: ")
		tydonorlastname = tydonorfullname.split()[1]
		#tydonorlook(tydonorselect)
		#donor_list(tydonorlookup, tydonoramount)
		donor_list(tydonorfullname, tydonoramount)
		tyletterprint(tydonorlastname, tydonoramount)
	elif tyaction == "2":
		addnewdonor()
	else:
		userinput()

def userinput():
	print ('''Please choose from one of the below options:\n
		To send a Thank You Note, enter T
		To create a report, enter R
		To exit, press Q\n''')
	action = input ("Enter Your Choice: ")
	if action == 'T' or action == 't':
		thankyounote()
	elif action == 'R' or action == 'r':
		createreport()
	else: 
		print ('Quitting program. Data will not be saved.')
		sys.exit()


if __name__ == '__main__':
	userinput()


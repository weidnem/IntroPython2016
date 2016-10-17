"""
This script should be executable. The script should accomplish the following goals:

It should have a data structure that holds a list of your donors and a history of the amounts they have donated. This structure should be populated at first with at least five donors, with between 1 and 3 donations each
The script should prompt the user (you) to choose from a menu of 2 actions: ‘Send a Thank You’ or ‘Create a Report’.
"""


#donors and their donation amounts
donors = {
"reginald": {1: 500, 2: 350, 3: 666},
"sassafrass": {1: 99},
"diggles": {1: 444, 2: 555}
}

prompt = """
To send a thank you note: enter "s"\n
To print a report: enter "r"\n
To quit: "q"\n
Choose an option:==>
"""

def sendThankyou():
    pass

def createReport():
    pass

def listDonors():
    for i in donors.keys():
    print(i)



if __name__ == "main":
    while true:
        response = input(prompt).strip
        if response == 'r':
            createReport()
        elif response == 's':
            sendThankyou()
        elif response = 'x':
            break
        else: print(Please enter your selection)

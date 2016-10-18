"""if __name__ == "__main__":

    response = ""
    while respose != "x":
        print("what do?\n, p")

        response = input("+>")

        if response == "p":
            printme()
"""
donor_1 = ["Jason Smith", 500, 500, 500]
donor_2 = ["Jane Doe", 5000]
donor_3 = ["Stevie Wonder", 8000, 52]
donor_4 = ["Mr. Man", 100, 75, 49]
donor_5 = ["The Dude", 666, 5]
master_list = [donor_1, donor_2, donor_3, donor_4, donor_5]


def donor_info(list):
    """separate master list into individual donors, and corresponding info."""

    #iterate master list to extract donor info
    count = 0
    for i in list:
        donor_name = i[0]
        history = i[1:]
        qty = len(i) - 1
        avg = sum(i[1:]) / (len(i) -1)
        print("%s, %s, %d, %d" %(donor_name, history, qty, avg))
        item_length(donor_name, history, qty, avg)
        count += 1
        #prevents formatter() from running prematurely, but causes item_length() to run an additional time.
        if count == len(list):
            col_size(item_length(donor_name, history, qty, avg))


def item_length(donor_name, history, qty, avg, widths=[]):
    """compare items under each heading. Determine column width based on longest string."""

    history_length = 0
    #history is passed as a list, so it's length must be determined iteratively.
    for i in history:
        history_length += len(str(i)) +2

    widths.append([len(donor_name)+2, history_length, len(str(qty))+2, len(str(avg))+2])
    return widths

def col_size(list):
    """Compare width info from item_length(). Determine max req'd column width for each element"""

    col_1 = []
    col_2 = []
    col_3 = []
    col_4 = []
    master_format = []

    for i in list:
        col_1.append(i[0])
        col_2.append(i[1])
        col_3.append(i[2])
        col_4.append(i[3])

    master_format = [max(col_1), max(col_2), max(col_3), max(col_4)]
    formatter(master_list, master_format)
    return master_format

def formatter(master_list, master_format):
   pass


donor_info(master_list)
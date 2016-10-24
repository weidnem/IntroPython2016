"""
Name: Paul Briant
Date: 10/24/16
Class: Introduction to Python
Session04
Assignment: Kata Fourteen

Description:

"""
# -------------------------------Import-----------------------------------------

# -------------------------------Functions--------------------------------------


def read_file(file_name):
    """
    Take in a file and return it as a string.
    """
    with open(file_name) as f:
        string = f.read()
    return string


def set_generator(string):
    """
    Iterate through strings in file and place first three in a set.
    """
    str_list = string.split()
    # Initialized set with first three words of file.
    trigrams = set([str_list[0], str_list[1], str_list[2]])
    tri_dict = {}

    del str_list[0]
    del str_list[1]
    del str_list[2]

    for item in str_list:
        # trigrams = set([item, ])



# Use the first two as a key in a dictionary and the third as the value.
# Update the set so that it moves through the file one word at a time.
# If key already exists, add new values.
# Once entire file has been iterated through:
# Choose random word pair as the start and use these to look up the next word.
# Write to file.
# Use second and third words to look up the next word.
#

# ==============================================================================


def main():
    """
    Tests output.
    """


if __name__ == '__main__':
    main()

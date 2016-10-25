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
    tri_dict = {}

    for i in range(len(str_list)):
        # Use the first two strings as a key in tri_dict.
        tri_key = str_list[i] + ' ' + str_list[i + 1]
        # Use the third string as the value tri_dict.
        tri_dict[tri_key] = str_list[i + 2]

    return tri_dict


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

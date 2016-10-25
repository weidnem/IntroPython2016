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


def dict_gen(string):
    """
    Take in a large string of all the words in the file. Split that string
    into a list of strings. Iterate through list of strings and concatenate
    focus item and item directely following it to create a dictionary key.
    Assign the next string as the value. Return dictionary.
    """
    str_list = string.split()
    tri_dict = {}

    for i in range(len(str_list)):
        # Use the first two strings as a key in tri_dict.
        tri_key = str_list[i] + ' ' + str_list[i + 1]
        # Check if key exists
        if tri_key not in tri_dict.keys():
            # Use the third string as the value tri_dict.
            tri_dict[tri_key] = [str_list[i + 2]]
        else:
            # If key already exists, add new values.
            tri_dict[tri_key].append(str_list[i + 2])

    return tri_dict


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

"""
Name: Paul Briant
Date: 10/24/16
Class: Introduction to Python
Session04
Assignment: Kata Fourteen

Description:

"""
# -------------------------------Import-----------------------------------------
import random
# -------------------------------Functions--------------------------------------


def read_file(file_name):
    """
    Take in a file and return it as a string.
    """
    with open(file_name) as f:
        string = f.read()
    return string


def gen_list(string):
    """
    Take in a large string of all the words in the file. Split that string
    into a list of strings.
    """
    str_list = string.split()
    return str_list


def dict_gen(str_list):
    """
    Take in a list of strings. Iterate through list of strings and concatenate
    focus item and item directely following it to create a dictionary key.
    Assign the next string as the value. Return dictionary.
    """
    tri_dict = {}

    for i in range(len(str_list)):
        # Ensures list index is in range
        if (i + 2) < len(str_list):
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


def key_lookup(str_list):
    """
    Once entire file has been iterated through:
    Choose random word pair as the start and use these to look up the next
    word.
    """
    rand_item = random.choice(str_list)
    item2_index = rand_item.index(str_list)
    item2 = str_list[item2_index]
    start_key = rand_item + ' ' + item2
    return start_key


# Write to file.
# Use second and third words to look up the next word.
#

# ==============================================================================


def main():
    """
    Tests output.
    """
    string = read_file('tri_test.txt')
    str_list = gen_list(string)
    print(dict_gen(str_list))

if __name__ == '__main__':
    main()

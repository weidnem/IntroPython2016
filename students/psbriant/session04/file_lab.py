"""
Name: Paul Briant
Date: 10/24/16
Class: Introduction to Python
Session04
LAB: File Lab

Description:
This program explores handling files and parsing simple text.

Questions:
When should we use 'with' and why?
To what degree should we handle exceptions?
"""
# -------------------------------Import-----------------------------------------
import pathlib
# -------------------------------Functions--------------------------------------


def print_path():
    """
    Display the absolute path of all files in the current directory one per
    line using pathlib. Zero arguments are accepted.
    """
    # Collect paths of files
    pth = pathlib.Path('./')
    # Iterate through files and print each absolute path
    for f in pth.iterdir():
        print(f.absolute())


def copy_file(file_name):
    """
    Takes in a file and copies it from the source to a destination.

    Questions:
    Correct method of specifying directory?
    Intended way of copying file?
    """
    lines = read_file(file_name)
    outfile = open(file_name, 'wb')
    for line in lines:
        outfile.write(line)
    outfile.close()


def read_file(file_name):
    """
    Takes in a file as the only argument, reads it and returns each line as a
    list of strings.
    """
    f = open(file_name, 'rb')
    lines = f.readlines()
    f.close()
    return lines


def list_languages(file_name):
    """

    """
    lines = read_file(file_name)
    languages = []
    for line in lines:
        strs = line.split(':')[1]
        lang = strs.split(',')
        for item in lang:
            item.strip()
            if item not in languages:
                languages.append(item)
    return languages




# ==============================================================================


def main():
    """
    Tests output.
    """
    # print_path()
    # copy_file()

if __name__ == '__main__':
    main()

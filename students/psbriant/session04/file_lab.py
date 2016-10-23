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


def copy_file(input_file, output_file):
    """
    Takes in a file and copies it from the source to a destination.
    """
    lines = read_file(input_file)
    with open(output_file, 'wb') as outfile:
        outfile.write(lines)
    outfile.close()


def read_file(file_name):
    """
    Takes in a file as the only argument, reads it and returns each line as a
    list of strings.
    """
    with open(file_name, 'rb') as f:
        lines = f.read()
    f.close()
    return lines


def r_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def list_languages():
    """
    Questions:
    What is the best way to get the path of desired file?
    Should we use a dictionary for the advanced segment?
    """
    lines = r_file('../../../Examples/Session01/students.txt')
    languages = []
    for line in lines:
        if ':' in line:
            strs = line.split(':')
            # print(strs)
            print(strs[1])
            lang_str = strs.pop(1)
            lang = lang_str.split(',')
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
    list_languages()


if __name__ == '__main__':
    main()

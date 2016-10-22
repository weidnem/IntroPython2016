"""
Name: Paul Briant
Date: 10/24/16
Class: Introduction to Python
Session04
LAB: File Lab

Description:
This program explores handling files and parsing simple text.
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
    """


# ==============================================================================


def main():
    """
    Tests output.
    """
    print_path()

if __name__ == '__main__':
    main()

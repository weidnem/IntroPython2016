"""
Name: Paul Briant
Date: 10/11/16
Class: Introduction to Python
LAB: grid printer

Description:
This program builds a grid based on specific size parameters.
"""
# -------------------------------Import-----------------------------------------

# -------------------------------Functions--------------------------------------


def grid_line():
    """
    Print each row of grid.
    """
    print('+' + (2 * ('-' * 4 + '+')))
    print((('|' + (2 * (' ' * 4 + '|')) + '\n') * 4), end='')
    print('+' + (2 * ('-' * 4 + '+')))
    print((('|' + (2 * (' ' * 4 + '|')) + '\n') * 4), end='')
    print('+' + (2 * ('-' * 4 + '+')))


def print_grid(char1, char2, char2num):
    """
    This function takes in two single character strings and one integer and
    prints each row of the grid as specified.
    """

# ==============================================================================


def main():
    """
    Builds a grid based on a specific character and size parameters.
    """
    grid_print()

if __name__ == '__main__':
    main()

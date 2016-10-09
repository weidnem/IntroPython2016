"""
Name: Paul Briant
Date: 10/11/16
LAB: grid printer
Description:
This program builds a grid based on specific size parameters.
"""
# -------------------------------Import-----------------------------------------

# -------------------------------Functions--------------------------------------


def grid_line(char1, char2, char2num, number):
    """
    This function takes in two single character strings and two integers and
    prints each row of the grid as specified.
    """
    for i in range(number):
        grid_line(char1, char2, char2num)

    return None


def print_grid(char1, char2, char2num):
    """
    This function takes in two single character strings and one integer and
    prints each row of the grid as specified.
    """
    print((char1 * 1) + (char2 * char2num) + (char1 * 1) + (char2 * char2num) +
          (char1 * 1))

    return None


# ==============================================================================
def main():
    """
    Builds a grid based on a specific character and size parameters.
    """
    print_grid('+', '-', 4)
    grid_line('|', ' ', 4, 4)
    print_grid('+', '-', 4)
    grid_line('|', ' ', 4, 4)
    print_grid('+', '-', 4)


if __name__ == '__main__':
    main()

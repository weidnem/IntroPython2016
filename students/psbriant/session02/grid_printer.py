"""
Name: Paul Briant
Date: 10/11/16
Class: Introduction to Python
LAB: grid printer

Description:
This program builds a grid based on specific size parameters.
"""
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


def print_grid(n):
    """

    """
    size = n // 2
    print('+' + (2 * ('-' * size + '+')))
    print((('|' + (2 * (' ' * size + '|')) + '\n') * size), end='')
    print('+' + (2 * ('-' * size + '+')))
    print((('|' + (2 * (' ' * size + '|')) + '\n') * size), end='')
    print('+' + (2 * ('-' * size + '+')))


def print_grid2(rc, s):
    """

    """
    print('+' + (rc * ('-' * s + '+')))
    print(((('|' + (rc * (' ' * s + '|')) + '\n') * s) +
          ('+' + (rc * ('-' * s + '+'))) + '\n') * rc, end='')

# ==============================================================================


def main():
    """
    Builds a grid based on a specific character and size parameters.
    """
    # grid_line()
    # print_grid(15)
    # print_grid(3)
    print_grid2(3, 4)
    print_grid2(5, 3)


if __name__ == '__main__':
    main()

"""
Name: Paul Briant
Date: 11/15/16
Class: Introduction to Python
Session05
LAB: Dictionaries

Description:

"""

# -------------------------------Imports----------------------------------------


# -------------------------------Functions--------------------------------------


def print_colors(fore_color='Blue', back_color='Green', link_color='White',
                 visited_color='Yellow'):
    """
    Take in strings representing the color of the foreground, background, links
    and visited links of a website and display the them.
    """
    print(fore_color, back_color, link_color, visited_color)

# ==============================================================================


def main():
    """
    Tests output.
    """
    print_colors()

if __name__ == '__main__':
    main()

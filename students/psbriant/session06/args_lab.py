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
    print("Foreground: {} Background: {} Links: {} Visited links: "
          "{}".format(fore_color, back_color, link_color, visited_color))


def print_colors2(**kwargs):
    """
    Take in strings representing the color of the foreground, background, links
    and visited links of a website and display the them.
    """
    print("Foreground: {fore_color} Background: {back_color}"
          " Links: {link_color} Visited"
          " links: {visited_color}".format(**kwargs))


# ==============================================================================


def main():
    """
    Tests output.
    """
    print_colors()
    print_colors('Purple')
    print_colors(back_color='Black', visited_color='Pink')

    print_colors2(fore_color='Blue', back_color='Green', link_color='White',
                  visited_color='Yellow')

if __name__ == '__main__':
    main()

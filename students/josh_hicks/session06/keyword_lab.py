#!/usr/bin/env python
'''
keyword arguments:

Write a function that has four optional parameters (with defaults):
fore_color
back_color
link_color
visited_color
Have it print the colors (use strings for the colors)
Call it with a couple different parameters set
Have it pull the parameters out with *args, **kwargs - and print those
'''


def set_colors(fore_color="white", back_color="black", link_color="blue",
               visited_color="grey"):
    print("{0}, {1} , {2}, {3}".format(fore_color, back_color, link_color,
                                        visited_color))


if __name__ == '__main__':
    set_colors()
    set_colors(fore_color="blue", link_color="white")

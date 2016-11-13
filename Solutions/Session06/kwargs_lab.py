#!/usr/bin/env python

"""
args-kwargs lab:

Experimenting with various ways to call and define functions

The colors function defined below is called in various ways by the test module:

test_kwargs_lab.py


"""

from collections import OrderedDict


def colors(fore_color='red',
           back_color='blue',
           link_color='green',
           visited_color='cyan',
           ):
    output = ("The colors are:\n"
              "  foreground: {fore_color}\n"
              "  background: {back_color}\n"
              "  link: {link_color}\n"
              "  visited: {visited_color}")
    output = output.format(fore_color=fore_color,
                           back_color=back_color,
                           link_color=link_color,
                           visited_color=visited_color)

    return output


def call_colors(*args, **kwargs):
    """
    this function has the most generic signature possible:

    you can pass ANYTHING in, and it will accept that.

    But the goal here is to explore the other side of the question:
      making sure you know what happens when this function is called
      in various ways.

    So this function will simpily return args and kwargs, and the test
    code will check and see if it works the way it is expected.

    As a rule, you don't want to do that -- you are throwing away Python's
    ability to check your arguments for you.

    *args and **kwargs should be saved for times when you NEED generic
    function processing. There are two common use cases for this:

    1) When you need to pass arguments through to antoher nested function --
        we'll see examples of this in OO programming with subclassing and
        some exampels of caling functions uknown at code writing time.
    2) When the arguments aren't known when you define the function:
       - either the number of arguments -- *args -- for example:
         os.path.join() function.
       - or any arbitrary keyword arguments, for example:
          str.format()

    """
    return args, kwargs


def colors_manual(*args, **kwargs):
    """
    This example to show you how much work you need to do to do this by hand!
    """
    # putting this in a tuple, as order is important
    #  could also use an ordereddict
    default_colors = OrderedDict((('fore_color', 'red'),
                                  ('back_color', 'blue'),
                                  ('link_color', 'green'),
                                  ('visited_color', 'cyan'),
                                  ))
    all_args = {}

    # unpack the args tuple:
    for i, key in enumerate(default_colors.keys()):
        try:
            all_args[key] = args[i]
        except IndexError:  # This will get raised when the tuple is exausted
            break

    for key, color in default_colors.items():
        if key in all_args:  # it's already been set
            if key in kwargs:  # it's a duplicate
                msg = "colors_manual() got multiple values for argument '{}'".format(key)
                raise TypeError(msg)
        elif key in kwargs:
            # set it from the kwargs dict
            all_args[key] = kwargs[key]
        else:
            # set it to the default
            all_args[key] = color

    output = ("The colors are:\n"
              "  foreground: {fore_color}\n"
              "  background: {back_color}\n"
              "  link: {link_color}\n"
              "  visited: {visited_color}")
    output = output.format(**all_args)

    return output

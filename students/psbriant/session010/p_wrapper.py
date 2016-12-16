#!/usr/bin/env python
"""
p_wrapper decorator
"""

def p_wrapper(function):
    def func(*args, **kwargs):
        string = function(*args, **kwargs)
        string = "{} {} {}".format("<p>", string, "</p>")
        return string
    return func

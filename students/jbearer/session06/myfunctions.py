#!/usr/bin/env/python3
"""
LAB: pytest
November 1, 2016
"""

def monkey_trouble(a_smile, b_smile):
    return a_smile is b_smile

def squirrel_play(temp, is_summer):
    if is_summer:
        if temp >= 60 and temp <= 100:
            return True
    else:
        if temp >= 60 and temp <= 90:
            return True
    return False

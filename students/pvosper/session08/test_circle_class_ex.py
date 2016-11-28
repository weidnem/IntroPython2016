#!/usr/bin/env python3

"""
tests for circle_class_ex
"""

import math

from circle_class_ex import Circle, Circle_d

# 1: create class called Circle
def test_radius():
    c = Circle(4)
    assert c.radius == 4

# 2: Add a “diameter” property, so the user can get the diameter of the circle
def test_diameter():
    c = Circle(5)
    assert c.diameter == 10

def test_change_radius():
    c = Circle(5)
    c.radius = 2
    assert c.diameter == 4

# 3: Set up the diameter property so that the user can set the diameter of the circle
def test_change_diameter():
    c = Circle(5)
    c.diameter = 12
    assert c.diameter == 12
    assert c.radius == 6

# 4: Add an area property so the user can get the area of the circle
def test_area():
    c = Circle(4)
    assert c.area == math.pi * 4**2

# 5: Add an “alternate constructor” that lets the user create a Circle directly with the diameter
def test_create_by_diameter():
    c = Circle_d(14)
    assert c.diameter == 14
    assert c.radius == 7
    assert c.area == math.pi * 7**2

# 6: Add __str__ and __repr__ methods to your Circle class (printing)
# 7: Add some of the numeric protocol to your Circle (add & multiply)
# 8: add the ability to compare two circles (<, >, &etc)
# 8: Optional Features
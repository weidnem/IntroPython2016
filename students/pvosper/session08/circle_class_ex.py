#!/usr/bin/env python3

"""
circle lab
1: create class called Circle
2: Add a “diameter” property, so the user can get the diameter of the circle
3: Set up the diameter property so that the user can set the diameter of the circle
4: Add an area property so the user can get the area of the circle
5: Add an “alternate constructor” that lets the user create a Circle directly with the diameter
6: Add __str__ and __repr__ methods to your Circle class (printing)
7: Add some of the numeric protocol to your Circle (add & multiply)
8: add the ability to compare two circles (<, >, &etc)
8: Optional Features

"""

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Get the diameter of the circle
    @property
    def diameter(self):
        return self.radius * 2

    # Set the diameter of the circle       
    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    # Get the area of the circle
    @property
    def area(self):
        return self.radius**2 * math.pi
    
# Create a Circle directly with the diameter
class Circle_d(Circle):
    def __init__(self, diameter):
        self.diameter = diameter
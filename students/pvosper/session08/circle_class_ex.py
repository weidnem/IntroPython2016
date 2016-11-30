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
    '''Creates circle object given a radius'''
    def __init__(self, radius):
        self.radius = radius

    # Get the diameter of the circle
    # @property is a decorator
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
    @classmethod
    def circle_d(cls, diameter):
        self = cls(diameter / 2)    # By convention use 'self'
        return self
        
    # __str__ and __repr__ methods to your Circle class (printing)
    # Ex: print(c): 'Circle with radius: 4.000000'
    def __str__(self):
        return 'Circle with radius: {:.6f}'.format(self.radius)
        
    # Ex: repr(c): 'Circle(4)'
    # eval( repr(something) ) == something
    def __repr__(self):
        return 'Circle({})'.format(self.radius)
    
    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    # Works (c * 3), but not for reflection (3 * c)
    # First arg always self!
#     def __mul__(*args): #self, other):
#         # return Circle(self.radius * other)
#         product = 1
#         for entry in args:
#             if hasattr(entry, 'radius'):
#                 print('entry.radius = ', entry.radius)
#                 product *= entry.radius
#             else:
#                 print('entry = ', entry)
#                 product *= entry
#         return Circle(product)
    
    def __gt__(self, other):
        a = self.radius
        b = other.radius
        return a > b

# All tests pass *without* this - why?
# ! lt assumed to be opposite of gt    
#     def __lt__(self, other):
#         a = self.radius
#         b = other.radius
#         return a < b
    
    def __eq__(self, other):
        a = self.radius
        b = other.radius
        return a == b
"""
Name: Paul Briant
Date: 11/29/16
Class: Introduction to Python
Session: 08
Assignment: Circle Lab

Description:
Classes for Circle Lab
"""

import math


class Circle:
    def __init__(self, radius):
        """ Initialize circle attributes radius and diameter"""
        self.radius = radius

        self.diameter = radius * 2

        @classmethod
        def from_diameter(cls, diameter):

            self = cls(diameter / 2)
            return self

        def __str__(self):
            return "A circle object with radius: {}".format(self.radius)

        def __repr__(self):
            return "Circle({})".format(self.radius)

        @property
        def diameter(self):
            """ Calculate diameter from radius"""
            return self.radius * 2

        @diameter.setter
        def diameter(self, value):
            """ Calculate radius from diameter"""
            self.radius = value / 2

        @property
        def area(self):
            """ Calculate area using radius and pi"""
            return (self.radius ** 2) * math.pi

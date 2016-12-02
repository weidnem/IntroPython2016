"""
Name: Paul Briant
Date: 11/29/16
Class: Introduction to Python
Session: 08
Assignment: Circle Lab

Description:
Classes for Circle Lab
"""


class Circle:
    def __init__(self, radius):
        """

        """
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
            return self.radius * 2

        @diameter.setter
        def diameter(self, value):
            self.radius = value / 2

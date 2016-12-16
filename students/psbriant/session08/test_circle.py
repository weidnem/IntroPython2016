"""
Name: Paul Briant
Date: 11/22/16
Class: Introduction to Python
Session: 08
Assignment: circle lab

Description:
Tests for Circle lab
"""

# -------------------------------Imports----------------------------------------
import math
from circle import Circle
# -------------------------------Functions--------------------------------------


def test_radius():
    """
    Test radius attribute
    """
    c = Circle(4)
    assert c.radius == 4


def test_diameter():
    """
    Test diameter attribute
    """
    c = Circle(5)
    assert c.diameter == 10


def test_change_radius():
    """
    Test ability for class to alter radius
    """
    c = Circle(5)
    c.radius = 2
    assert c.diameter == 4


def test_change_diameter():
    """
    Test ability for class to alter diameter
    """
    c = Circle(5)
    c.diameter = 12
    assert c.diameter == 12
    assert c.radius == 6


def test_area():
    """
    Verify area of circle
    """
    c = Circle(5)
    assert c.area == 25

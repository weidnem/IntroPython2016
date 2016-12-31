#!/usr/env/python3

import math
from circle import Circle


def test_radius():
    c = Circle(4)
    assert c.radius == 4


def test_diameter():
    c = Circle(5)
    assert c.diameter == 10

# def test_change_radius():
#     c = Circle(5)
#     c.radius = 2
#     assert c.diameter == 4


def test_change_radius():
    c = Circle(5)
    c.radius = 2
    assert c.diameter == 4


def test_change_diameter():
    c = Circle(5)
    c.diameter = 12
    assert c.diameter == 12
    assert c.radius == 6

def test_area():
    c = Circle(5)
    assert c.area == math.pi * 4
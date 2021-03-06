#!/usr/bin/env python

'''
tests for circle class
'''

from circle import Circle
import math


def test_radius():
    c = Circle(4)
    assert c.radius == 4


def test_diameter():
    c = Circle(5)
    assert c.diameter == 10


def test_change_radius():
    c = Circle(5)
    c.radius = 2
    assert c.diameter == 4


def test_change_diameter():
    c = Circle(6)
    c.diameter = 12
    assert c.diameter == 12
    assert c.radius == 6


def test_area():

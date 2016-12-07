'''Session08 : Test circle_lab '''
import math
from circle_lab import Circle

def test_getter():
	c = Circle()
	res = c.rad
	assert 1 is res

def test_setter():
	c = Circle()
	c.rad = 4
	res = c.rad
	assert 4 is res

def test_diameter():
	c = Circle()
    # should be 1 by default
	res = c.rad
	assert 1 is res
	# set diameter and radius should be half of that
	c.diameter = 6
	res = c.rad
	# should be converted to int
	assert 3 is int(res)

def test_area():
	c = Circle()
	res = c.area
	pi_val = math.pi
	#  throws an assertion area when using "is"
	assert pi_val == res

def test_repr():
	ans = "Circle (4)"
	c = Circle(4)
	res = c.__repr__()
	#  'is' checks if both the operands are the same object
	#  '==' checks for equality
	assert ans == res



#Test for circle class

from circle import Circle

def test_radius():
	c = Circle (4)
	assert c.radius == 4

def test_diameter():
	c = Circle (5)
	assert c.diameter  == 10

def change_radius():
	c = Circle (5)
	c.radius = 2
	assert c.diameter == 4
	
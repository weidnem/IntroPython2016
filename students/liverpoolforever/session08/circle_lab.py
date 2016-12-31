''' Session08 : OOO continued with getter and setter behavior'''

import math

# class C:
# 	# """ Getter and Setter method should have same name "val" """
#     _x = None  # underscore is for private attributes
#     @property
#     def val(self):
#     	"""I am read only"""
#     	return self._x
#     @val.setter
#     def val(self, value):
#         self._x = value
class Circle:
    radius = None  # do we need this?
    def __init__(self,def_val=1):
        self.radius = def_val
    # 2nd constructor
    @property
    def rad(self):
        return self.radius
    @rad.setter
    def rad(self,val):
        self.radius = val
    @property
    def diameter(self):
        dia = self.radius*2
        return dia
    @diameter.setter
    def diameter(self,val):
        dia = val
        self.radius = dia/2
    @property
    def area(self):
        area = math.pi * self.radius **2 
        return area
    def __str__(self):
        """ Overrides default method - print(c) will call this method"""
        read_str = "Circle with radius: {:d}".format(self.radius)
        return read_str
    def __repr__(self):
        """Overrides default method - only typing c in console will call this method"""
        # pretty_str = "Circle (" + self.radius + ")"
        pretty_str = "Circle ({})".format(self.radius)
        return pretty_str

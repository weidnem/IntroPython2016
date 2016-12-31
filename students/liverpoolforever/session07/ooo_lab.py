#!/bin/bash
''' oo lab '''


class Point:
    size = 4
    color= "red"

    # def __init__(self):
    # 	self = self

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __init__(self,size,color):
    	'''Does overload the init method'''
    	self.size = size
    	self.color = color

    def get_color(self):
    	''' self needs to be passed to each method'''
    	return self.color

def main():
	# pt = Point(5,'blue')
	pt2 = Point(3,2)
	# result = pt2.get_color()
	print("Color is :" , pt2.get_color())

if __name__ == '__main__':
	main()


"""this is a lab to create grid patterns"""

#first version simple print statement
def grid_printer():
    print('+ - - - - + - - - - +')
    print('|         |         |')
    print('|         |         |')
    print('|         |         |')
    print('|         |         |')
    print('+ - - - - + - - - - +')
    print('|         |         |')
    print('|         |         |')
    print('|         |         |')
    print('|         |         |')
    print('+ - - - - + - - - - +')

#version 2 using values as print objects
def print_grid(n):
    sides = "|"
    apex = "+ "
    topBottom = "- "
    top = apex+topBottom*n+apex+topBottom*n+apex
    wall = sides+"  "*(n)+" "
    count = n
    print(top)
    wallMaker(n)
    print(top)
    wallMaker(n)
    print(top)

#top helper method
def topMaker(n,squares):
    apex = "+ "
    lines = "- "
    top = ((apex+lines*n)*squares)+apex
    print(top)

#wall making helper method
def wallMaker(n,squares):
    count = n
    sides = "|"
    wall = sides+"  "*(n)+" "
    #loops through to make enough walls
    while count !=0:
        print(wall*(squares+1))
        count -= 1

#main grid making method
def print_grid2(squares,size):
    counter = squares
    #loop to print the boxes
    while counter != 0:
        topMaker(size,squares)
        wallMaker(size,squares)
        counter -=1
    topMaker(size, squares)


def main():
    squares = eval(input("How many squares would you like? "))
    size = eval(input("what size squares would you like? "))
    print_grid2(squares, size)

main()

#print_grid2(3,4)
#print()
#print_grid2(5,3)
#print()
#print_grid2(2,6)
#print()
#print_grid2(9,1)












    
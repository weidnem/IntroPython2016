"""
grid printer
"""

def cheat_grid():
    print("+ - - - - + - - - - +\n|         |         |\n|         |         |\n|         |         |\n|         |         |\n+ - - - - + - - - - +\n|         |         |\n|         |         |\n|         |         |\n|         |         |\n+ - - - - + - - - - +")

def slightly_less_of_a_cheat_grid():
    print("+"+" -"*4+" +"+" -"*4+" +")
    print("|"+" "*9+"|"+" "*9+"|")
    print("|"+" "*9+"|"+" "*9+"|")
    print("|"+" "*9+"|"+" "*9+"|")
    print("|"+" "*9+"|"+" "*9+"|")
    print("+"+" -"*4+" +"+" -"*4+" +")
    print("|"+" "*9+"|"+" "*9+"|")
    print("|"+" "*9+"|"+" "*9+"|")
    print("|"+" "*9+"|"+" "*9+"|")
    print("|"+" "*9+"|"+" "*9+"|")
    print("+"+" -"*4+" +"+" -"*4+" +")

def configureable_grid(size):
    height_width = size-1
    spaces = (size*2)-1
    print("+"+" -"*height_width+" +"+" -"*height_width+" +")
    for i in range(height_width):
        print("|"+" "*spaces+"|"+" "*spaces+"|")
    print("+"+" -"*height_width+" +"+" -"*height_width+" +")
    for i in range(height_width):
        print("|"+" "*spaces+"|"+" "*spaces+"|")
    print("+"+" -"*height_width+" +"+" -"*height_width+" +")

#cheat_grid()
#slightly_less_of_a_cheat_grid()
configureable_grid(10)
"""Simple text grid drawing script
10/7/16 edit. Moved input typing to function call and eliminated redundant variables to shorten code and improve readability. 
"""

ROWS = input("Rows: ")
COLUMNS = input("Columns: ")
SIZE = input("Size: ")

def print_grid(rows, columns, size):

    corner = "+"
    h_part = "-"
    space = " "
    v_part = "|"

    h_separator = ((space + h_part) * size) + space
    v_separator = v_part + (space * ((size * 2 ) + 1))

    for n in range(rows):
        for i in range(columns):
            print(corner + h_separator, end="")
        print(corner)

        for n in range(size):
            for i in range(columns):
                print(v_separator, end="")
            print(v_part)
    for n in range(columns):
        print(corner + h_separator, end="")
    print(corner)

print_grid(int(ROWS), int(COLUMNS), int(SIZE))


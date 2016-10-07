"""Simple text grid drawing script
"""

ROWS = input("Rows: ")
COLUMNS = input("Columns: ")
SIZE = input("Size: ")

def print_grid(rows, columns, size):
    corner = "+"
    h_part = "-"
    space = " "
    v_part = "|"

    h_separator = ((space + h_part) * int(size)) + space
    v_separator = v_part + (space * ( (int(size) * 2 ) + 1))

    height = int(size)
    count1 = int(COLUMNS)
    count2 = int(ROWS)

    for n in range(count2):
        for i in range(count1):
            print(corner + h_separator, end="")
        print(corner)

        for n in range(height):
            for i in range(count1):
                print(v_separator, end="")
            print(v_part)
    for n in range(count1):
        print(corner + h_separator, end="")
    print(corner)

print_grid(ROWS, COLUMNS, SIZE)


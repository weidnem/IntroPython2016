"""Simple text grid drawing script
"""

ROWS = input("Rows: ")
COLUMNS = input("Columns: ")
SIZE = input("Size: ")


def print_grid(rows, columns, size):
    corner = "+"
    h_sep = " - "
    space = " "
    v_sep = "|"

    h_separator = h_sep * int(size)
    make_v_sep = v_sep * int(size)

    count1 = int(COLUMNS)
    count2 = int(ROWS)

    for n in range(count1):
        print(corner, end="")
        print(h_separator, end = "")
        print(corner, end = "")


print_grid(ROWS, COLUMNS, SIZE)


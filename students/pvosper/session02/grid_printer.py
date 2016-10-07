# cell: size of each cell
# grid: # of cells to print
# aspect: affects ratio of height to width (2 = square-ish)

bar = "|"
plus = "+"
minus = "-"
space = " "

def print_grid(cell = 3, grid = 2, aspect = 2):
    for i in range(grid):
        # horizontal
        for i in range(grid):
            print(plus+minus*(cell), end = "-")
        # close horizontal (only 1 is needed)
        print(plus)
        # verticals
        for i in range(cell-aspect):
            for i in range(grid):
                print(bar+space*(cell), end = " ")
            # close every vertical
            print(bar)
    # closing horizontal
    for i in range(grid):
        print(plus+minus*(cell), end = "-")
    print(plus)

print_grid(5,8,2)
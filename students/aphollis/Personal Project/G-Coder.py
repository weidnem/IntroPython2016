"""
G-Coder by Adam Hollis, 2016.
G-Coder allows simple operations to be programmed and cut on a basic CNC router without knowledge of CAM or G-Code programming.
"""

from textwrap import dedent, fill

def run_ui():
    """Print the main UI to the screen and get user input."""

    ui_text = fill(dedent("Select an operation from the menu below.  To generate multiple operations, enter each one separated by a comma, in the order of execution.  (ex: S, O, P)"), 90, break_long_words = False)

    print('{:<}'.format(ui_text))

    what_do = input(dedent('''

        (S) - Surface
        (P) - Profile
        (O) - Pocket
        (Q) - Quit\n\n

            '''))

    what_do = what_do.lower()
    what_do.strip()

    action = what_do.split(',')
    return action

def dims():

    print('Enter dimensions in inches: ')
    length = float(input('Length: '))
    width = float(input('Width: '))
    height = float(input('Height: '))

    return [length, width, height]

def surface():
    start_size = dims()
    final_size = input("Enter finished thickness: ")
    print('Generating G-Code to surface from {}" to {}"\n'.format(start_size[2], final_size))

    return geominatrix(start_size).coordinator()

def profile():
    size = dims()
    return geominatrix(size).coordinator()

def pocket():
    print('pocket!\n')

def quit():
    return False

def chain_input(list):
    #sort input list, string together multiple operations.

    for item in list:
        if item == 's':
            surface()
        elif item == 'p':
            profile()
        elif item == 'o':
            pocket()
        elif item == 'q':
            quit()
            return False
        else:
            print('Selection Invalid!')
            break

class geominatrix:
    """convert user input size to relative machine coordinates"""
    #tool number:radius
    tool_library = {1: 1.5625, 2: .125, 3: .25, 4: .09375}
    """converts user input for L x W x H into machine coordinates."""
    def __init__(self, list, tool = tool_library[3]):
         self.T = tool
         self.x = list[0]
         self.y = list[1]
         self.z = list[2]

    def coordinator(self, origin=(5, 5, 0)):
        """rework, tool offset needs to be a total net plus to overall dimensions...for profile, or a net minus for pocketing"""

        """!!!!!!ORDER IS WRONG FOR CW (CLIME) OPERATION"""

        tool_offset = ((origin[0] - self.T), (origin[1] - self.T), origin[2])

        first = origin[0] + self.x
        second = origin[1] + self.y
        third = origin[0]
        fourth = origin[1]

        print(dedent('''
            G0 X{0} Y{1} Z{2}
            {3} X{4}
            {3} Y{5}
            {3} X{6}
            {3} Y{7}
            ''').format(origin[0], origin[1], self.z, 'G1', first, second, third, fourth))

class g_man:
    pass

#(T = 3, S = 12000, F = 100)

if __name__ == "__main__":
    running = True
    print("\n\n******Welcome to G-Coder Beta******\n")

    while running:
        selection = run_ui()
        #run chain input, w/ quit check
        if chain_input(selection) == False:
            really = input('\nAre you sure you want to Quit? Y/N:\n')
            if really.lower() == 'y':
                running = False
            elif really.lower() == 'n':
                print('\n')
                running = True
            else:
                print('invalid selection')








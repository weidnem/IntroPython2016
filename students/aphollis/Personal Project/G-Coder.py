"""
G-Coder by Adam Hollis, 2016.
G-Coder allows simple operations to be programmed and cut on the Shop Sabre IS510 Router without knowledge of CAM or G-Code programming.
Basic changes will allow G-coder to be used for any G-Code compatible CNC router.
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

    return(action)


def dims():
    print('Enter part dimensions in inches: ')
    length = input('Length: ')
    width = input('Width: ')
    height = input('Height: ')

    return [length, width, height]

def surface():
    start_size = dims()
    final_size = input("Enter finished thickness: ")
    print('Generating G-Code to surface from {}" to {}"\n'.format(start_size[2], final_size))


def profile():
    print('profile!\n')

def pocket():
    print('pocket!\n')

def chain_input(list):

    count = len(list)
    while count >= 0:
        for item in list:
            if item == "s":
                count -= 1
                surface()
            elif item == "p":
                count -= 1
                profile()
            elif item == "o":
                count -= 1
                pocket()
            elif item == "q":
                return 'quit'
            else:
                print("error: menu selection is invalid!")

if __name__ == "__main__":
    running = True
    print("******Welcome to G-Coder Beta******")

    while running:
        selection = run_ui()
        chain_input(selection)
        if chain_input(selection) == 'quit':
            running = False





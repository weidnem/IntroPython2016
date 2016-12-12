"""
G-Coder(CNC Panel Saw) by Adam Hollis, 2016.
G-Coder allows simple sheet cutting operations to be programmed and cut on a basic CNC router without knowledge of CAM or
G-Code programming.

Generating usable G-Code turned out to be more challenging than anticipated and I ran out of time, so this just outputs.
to the console, rather than a file.

This will actually run on a CNC router, but it's far from optimized, and runs a superfluous cut at the end of each
operation that i haven't figured out how to remove yet.

Looking forward to making this Way better over the next couple months.
"""

from textwrap import dedent, fill
import sys
from io import StringIO


def run_ui():
    """Print the main UI to the screen and get user input."""

    ui_text = fill('''Choose an operation from the menu below. This program is only intended for .75" sheet goods. Enter an operation followed by a number to make multiple cuts (ex: R3)''', 100, break_long_words=False)

    print('{:<90}'.format(ui_text))

    what_do = input(dedent('''

        (R) - Rip
        (X) - Cross Cut
        (Q) - Quit\n\n

        '''))

    what_do = what_do.lower()
    action = what_do.strip()

    return action


# def cut_qty(str):
#
#     # add a cut qty if user entered none
#     if len(str) < 2:
#         str += '1'
#
#     return str[1:]

def cut_qty(qty, operation):
    """checks number of cuts * width vs sheet size, then passes to geominatrix for g-code generation"""
    qty = int(qty)
    x = float(input('Enter cut width(inch-decimal): '))
    output = [x, qty]
    if operation == 'xcut':
        sheet = 96.5
    else:
        sheet = 48.5

    if (qty * x) > (sheet - (qty * .25)):
        print('You can\'t get {} {}\" {} out of a sheet\n'.format(qty, x, operation))

        if operation == 'xcut':
            cut_qty(qty, 'xcut')
            return operation

        elif operation == 'rip':
            cut_qty(qty, 'rip')
            return operation

    # Here we go!
    Geominatrix(output).coordinator(operation)


def cut_type(menu_obj):

    # check for quit input
    if menu_obj == 'q':
        return False

    else:
        # Program requires a cut quantity, adds 1 if int not present.
        try:
            menu_obj[1]
        except IndexError:
            menu_obj += '1'

        if menu_obj[0] == 'r':

            cut_qty(menu_obj[1:], 'rip')
            # rip(qty)

        elif menu_obj[0] == 'x':
            cut_qty(menu_obj[1:], 'xcut')
            # (str)

        else:
            print('\nSelection Invalid!\n')


class Geominatrix:
    """Generates G-Code strings based on user input and cut type."""

    def __init__(self, list):
        self.width = float(list[0])
        self.count = int(list[1])

    # Counter to generate cuts line-by-line
    def coordinator(self, type, origin=(5, 5, 0)):
        count = self.count + 2  # + 2 or you don't get enough y-axis cuts.
        step = self.width
        start_x = origin[0]
        start_x -= step
        start_y = origin[1]
        start_y -= step
        flipper = True

        GWrapper.start() # Static wrapper for machine start
        # Code for Y-axis cuts
        if type == 'rip':
            while count >= 1:
                count -= 1
                start_x += step
                # flip Y coordinate from start to end
                if flipper is True:
                    y_coord = origin[1] - 1
                    flipper = False
                else:
                    y_coord = origin[1] + 96.5
                    flipper = True

                print('G1 Y{0}\nG1 X{1}'.format(y_coord, start_x))

        # same thing for cross-cutting
        elif type == 'xcut':
            while count >= 1:
                count -= 1
                start_y += step
                # flip X coordinate from start to end
                if flipper is True:
                    x_coord = origin[0] - 1
                    flipper = False
                else:
                    x_coord = origin[1] + 48.5
                    flipper = True

                print('G1 X{0}\nG1 Y{1}'.format(x_coord, start_y))


        GWrapper.stop() # static wrapper for machine stop


class GWrapper:
    """Wrapper for static machine start/stop parameters"""

    @staticmethod
    def start():
        # Positioning = Absolute, Spindle Off, Tool Check/Change, Spindle Speed, Spindle On, Jog to Start, Z down, Set Feed
        print(dedent('''
            G90
            M5
            T2
            S12000
            M3
            G0 X5 Y4 Z1
            Z0 F100
            '''))

    @staticmethod
    def stop():
        # Spindle power off, retract head, return home
        print(dedent('''
            M5
            G53 Z
            X0Y0
            '''))
        sys.exit(0)


if __name__ == "__main__":
    running = True
    title = '****** Welcome to CNC Panel Saw Beta ******'
    print('\n\n\n\n{:^90}\n'.format(title))

    while running:
        selection = run_ui()
        start = cut_type(selection)

        # run cut_type, w/ quit check
        if start is False:
            really = input('\nAre you sure you want to Quit? Y/N:\n')
            if really.lower() == 'y':
                running = False
            elif really.lower() == 'n':
                print('\n')
                running = True
            else:
                print('invalid selection')








"""-----Slicing Lab----
Goal
    Get the basics of sequence slicing down

Tasks
    Write some functions that:

    -return a sequence with the first and last items exchanged.
    -return a sequence with every other item removed
    -return a sequence with the first and last 4 items removed, and every other item in between
    -return a sequence reversed (just with slicing)
    -return a sequence with the middle third, then last third, then the first third in the new order
            NOTE: these should work with ANY sequence – but you can use strings to test, if you like.
"""

def start_end_reverse(a):
    i, j = a[0], a[-1]
    a[0] = j
    a[-1] = i
    print(a)
    return a

def rem_every_other(b):
    b = b[::2]
    print (b)
    return b

def rem_stuff(c):
    c = c[4:]
    c = c[:-4:1]
    print(c[::2])
    return c[::2]

def reverse_list(d):
    print(d[::-1])

def shell_game(e):
    """not equipped for handling lists not divisible by 3, how?"""
    thirds = len(e)//3
    first = e[:thirds]
    middle = e[thirds:thirds*2]
    last = e[thirds*2:]
    print(middle + last + first)





start_end_reverse([1,3,4,5,6,7,8,8,9,9])
rem_every_other([1,3,4,5,6,7,8,8,9,9])
rem_stuff([1,3,4,5,6,7,8,8,9,9])
reverse_list([1,3,4,5,6,7,8,8,9,9])
shell_game([1,3,4,5,6,7,8,8,9,9])
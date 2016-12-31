#!/usr/bin/env python

'''
write a program which prints the full path to all files in the current
directory, one per line

write a program which copies a file from a source,
to a destination (without using shutil, or the OS copy command)
    advanced: make it work for any size file: i.e. don’t read the entire
    contents of the file into memory at once.
'''


import os


def print_full_path():
    for f in os.listdir('.'):
        if os.path.isfile(f):
            print("{0}\{1}".format(os.getcwd(), f))


if __name__ == '__main__':
    print_full_path()

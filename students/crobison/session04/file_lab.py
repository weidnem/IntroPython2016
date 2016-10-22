# Charles Robison
# 2016.10.21
# File Lab

#!/usr/bin/env python
import os

cwd = os.getcwd()

# write a program which prints the full path to all files
# in the current directory, one per line
for item in os.listdir(cwd):
    print(cwd + "/" + item)

# write a program which copies a file from a source, to a
# destination (without using shutil, or the OS copy command)
file = open('file_lab01.txt', 'r')
file_text = file.read()
file_new = open('file_lab02.txt', 'w')
file_new.write(file_text)
file.close()
file_new.close()

# advanced: make it work for any size file: i.e. don’t read
# the entire contents of the file into memory at once.
file = open('file_lab01.txt', 'r')
file_new = open('file_lab02.txt', 'w')
file_text = file.readline()
for line in file_text:
    file_new.write(line)
    line = file.readline()
file.close()
file_new.close()

# not working correctl, second try:
print('second try:')

file_new = open('file_labe02.txt', 'w')
with open('file_lab01.txt', 'r') as f:
    for line in f:
        file_text = f.readline()
        file_new.write(line)
file_new.close()

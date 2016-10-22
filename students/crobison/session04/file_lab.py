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
with open('file_lab01.txt','r') as r, open('file_lab02.txt', 'w') as w:
    for line in r:
        w.write(line)
r.close()
w.close()



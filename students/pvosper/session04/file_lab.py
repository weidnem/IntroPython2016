#!/usr/bin/env python3

# === File Lab Exercises ===

# === Paths and File Processing ===

'''
Write a program which prints the full path to all files in the current 
directory, one per line
'''

import os

print(os.getcwd(), ":")

directory_list = os.listdir()

for entry in directory_list:
    print("\t", entry)

'''
Write a program which copies a file from a source, to a destination (without 
using shutil, or the OS copy command)
'''

# === CHB Example:

# with open(the_filename, 'w') as outfile:
#     outfile.write(something)
#     do_some_more...
# # now done with out file -- it will be closed, regardless of errors, etc.
# do_other_stuff

# Function to create 80 character line of gibberish
def line_of_gibberish():
    import random
    line = ""
    for i in range(80):
        line = line + chr(random.randint(41,79)) #$Todo: hex
    line = line + "\n"
    return line

# Create file to use as source
file_object = open('source_file.txt', 'w')
for i in range(100):
    file_object.write(line_of_gibberish())
file_object.close()

# Copy source to target line by line
target_file_object = open('target_file.txt','w')
source_file_object = open('source_file.txt','r')
while True:
    line = source_file_object.readline()
    if not line:
        break
    else:
        target_file_object.write(line)
target_file_object.close()
source_file_object.close()


# with open(temp_file.txt, 'rb') as infile, open(dest, 'wb') as outfile:
#     outfile.write(infile.read())



# temp_file = open('../../../Examples/Session01/students.txt')
# text_string = temp_file.read()
# temp_file.close()

d = {}

for line in open('../../../Examples/Session01/students.txt'):
    s = []
    s = line.split(':')
    if len(s) == 2:
        d[s[0]] = s[1].replace('\n', ' ')
    else:
        d[s[0]] = '<n/a>'

# for entry in d:
#     print(entry)

# .strip().lower()

# f = open('myfile','w')
# f.write('hi there\n') # python will convert \n to os.linesep
# f.close() # you can omit in most cases as the destructor will call it

if __name__ == '__main__':
    print('\n=== MAIN ===\n')

#     print(d)
#     print(d.values())
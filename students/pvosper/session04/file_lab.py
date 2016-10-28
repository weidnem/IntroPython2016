#!/usr/bin/env python3

# === File Lab Exercises ===

# === Paths and File Processing ===

'''
Write a program which prints the full path to all files in the current 
directory, one per line
'''

import os

# print full path to current directory
print(os.getcwd(), ":")

# create list of all files in current directory
directory_list = os.listdir()

# print each entry on it's own line
for entry in directory_list:
    print("\t", entry)

'''
Write a program which copies a file from a source, to a destination (without 
using shutil, or the OS copy command)
'''

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

# Create a dictionary from students.txt file
# key = name, value = languages
students_dictionary = {}

for line in open('../../../Examples/Session01/students.txt'):
    student_info = []
    student_info = line.split(':')
    if len(student_info) == 2:
        students_dictionary[student_info[0]] = student_info[1].replace('\n', ' ')
    else:
        students_dictionary[student_info[0]] = '<n/a>'

# Create a dictionary of languages
# key = language, value = count
# $todo value = list of students who know that language
# BUG: Header "Students Languages"
language_dictionary = {}
language_list = students_dictionary.values()
# print(language_list)
for entry in language_list:
    entry = entry.lower().replace(',', '').replace('pyton', 'python')
    entry_list = entry.split()
#     print(type(entry_list), entry_list)
    for language in entry_list:
#         print(language)
        if language in language_dictionary:
            language_dictionary[language] = language_dictionary[language] + 1
        else:
            language_dictionary[language] = 1

for languages in language_dictionary:             
    print(languages, language_dictionary[languages])

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
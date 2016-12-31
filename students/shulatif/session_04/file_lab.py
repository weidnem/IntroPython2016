import os
from collections import Counter as counter
from pprint import pprint


# write a program which prints the full path to all files in the current directory, one per line

for thing in os.listdir('.'):
    print(os.path.abspath(thing))

# write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command)
#      advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.
#      Note that if you want it to do any kind of file, you need to open the files in binary mode: open(filename, 'rb')
#      (or 'wb' for writing.)

source = 'gg.jpg'
dest = 'gg2.jpg'

with open(source, 'rb') as s, open(dest, 'wb') as d:
    print('Copying the contents now.')
    data_copy = s.readlines()
    print('Writing the contents to new file now.')
    d.writelines(data_copy)
    s.close()
    d.close()
    print('Closed files')


# Write a little script that reads that file, and generates a list of all the languages that have been used. students.txt
# Extra credit: keep track of how many students specified each language.

student_file = open('students.txt', 'r')
lang_set = set()
lang_list = []
with student_file:
    for student in student_file:
        languages = student.split(':')[1].lower()
        lang = languages.replace(',', ' ').split()
        for langs in lang:
            if langs == 'languages':
                pass
            elif langs:
                lang_set.add(langs)
                lang_list.append(langs)
    student_file.close()
    pprint('All the languages people in our class know:')
    pprint(' '.join(lang_set))
    pprint('How many people know each language:')
    pprint(counter(lang_list))




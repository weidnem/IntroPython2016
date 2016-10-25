#!/usr/bin/env python3

'''
File Lab Excercises.

'''

# temp_file = open('../../../Examples/Session01/students.txt')
# text_string = temp_file.read()
# temp_file.close()


d = {}

for line in open('../../../Examples/Session01/students.txt'):
    s = []
    s = line.split(':')
    if len(s) == 2:
        d[s[0]] = s[1]
    else:
        d[s[0]] = '<n/a>'

if __name__ == '__main__':
    print('\n=== MAIN ===\n')

    print(d)
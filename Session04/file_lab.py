#!/usr/bin/env python3

'''
File Lab Excercises.


'''

# student_text = open('../IntroPython2016/Examples/Session01/students.txt')
students_file = open('../IntroPython2016/Examples/Session01/students.txt')
d = {}
s = students_file.readline()
print(s)
students_string = students_file.read()#. replace('\n', ' ')
students_file.close()
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 09:20:55 2016

@author: noner_000
"""

import os
import pathlib

pathname = "C:/Python2016/IntroPython2016/Examples/Session01/"
filename = "students.txt"
langs = set()

with open(pathname+filename, 'r') as f:
    for line in f:
        if len(line[line.find(":"):].split(',')) > 0:
            items = line[line.find(":")+2:line.find("\n")].split(',')
            for lang in items:
                langs.add(lang.strip())
#        print(langs)
print(langs)
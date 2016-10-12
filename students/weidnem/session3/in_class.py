# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 18:58:58 2016

@author: noner_000
"""

s = [1,2,3,4,5,6,7,8,9,10,11]
print(s)
r = [s[-1]] + s[1:-1] + [s[0]]
print(r)
q = s[::2]
print(q)
p = s[4:-4:2]
print(p)
o = s[::-1]
print(o)
n =  s[int(len(s)/3):int(len(s)/3)*2] + s[int(len(s)/3)*2:] +  s[:int(len(s)/3)]
print(n)
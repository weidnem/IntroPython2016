# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 18:08:27 2016

@author: noner_000
"""

import codecs

def rot13 (txt):
    txt = codecs.encode(txt,'rot-13')
    return txt

def derot13 (txt):
    txt = codecs.decode(txt,'rot-13')
    return txt
    

if __name__ == '__main__':
    
    #insert asserts here to test functions when run as standalone
    print(rot13("wiggle wobble"))
    print("Good To Go! Let's Rot!")
#!/usr/bin/env python3
"""
Excercise --  ROT13
October 13, 2016
"""

if __name__ == '__main__':

    def rot13(myStr):
        alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        key =   'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'

        decoder = str.maketrans(alpha,key)

        answer = myStr.translate(decoder)

        print(answer)

    theStr = 'Zntargvp sebz bhgfvqr arne pbeare' 

    rot13(theStr)



        
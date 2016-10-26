#!/usr/bin/env/python3
"""
LAB: Trigrams
October 20, 2016
"""

import random

def trigram_fun():
    with open('sherlock.txt','r') as file_in:
        my_book = file_in.read()
    file_in.close()

    my_book = my_book.replace('\n', ' ')

    l_book = []
    l_book = my_book.split(' ')

    bigram_list = list(zip(l_book,l_book[1:]))
    trigram_list = list(zip(l_book,l_book[1:],l_book[2:]))

    dict_list = {}
    for i in range(len(trigram_list)):
        tri_key = trigram_list[i][0] + ' ' + trigram_list[i][1]
        tri_value = trigram_list[i][2]
        if tri_key in dict_list:
            dict_list[tri_key].append(tri_value)
        else:
            dict_list[tri_key] = [tri_value]


    new_tri = []
    myStr = trigram_list[2000][0] + ' ' + trigram_list[2000][1]
    if myStr in dict_list.keys():
        new_tri.append(trigram_list[2000][0])
        new_tri.append(trigram_list[2000][1])
        # print('myStr:',myStr)
        # print('Values:',dict_list[myStr])
        # print('new_tri:',new_tri)
        rand_value = random.randrange(len(dict_list[myStr])-1)
        # print('rand_value:',rand_value)
        # print('Appending:',dict_list[myStr][rand_value])
        new_tri.append(dict_list[myStr][rand_value])
    else:
        print('no')

    for i in range(20):
        myStr = new_tri[-2] + ' ' + new_tri[-1]
        rand_value = random.randrange(len(dict_list[myStr])-1)
        new_tri.append(dict_list[myStr][rand_value])

        print('myStr:',myStr)
        print('dict_list',dict_list[myStr])
        print()
        
    print('new_tri:',new_tri)


    # for k, v in dict_list.items():
    #     print('Keys:',k,'\n','Values:',v)


trigram_fun()
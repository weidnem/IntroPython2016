#!/usr/bin/env/python3
"""
LAB: Trigrams
October 20, 2016
"""

def trigram_fun():
    with open('sherlock.txt','r') as file_in:
        my_book = file_in.read()
    file_in.close()

    my_book = my_book.replace('\n', ' ')

    l_book = []
    l_book = my_book.split(' ')

    trigram_list = list(zip(l_book,l_book[1:],l_book[2:]))

    dict_list = {}
    for i in range(len(trigram_list)):
        tri_key = trigram_list[i][0] + ' ' + trigram_list[i][1]
        tri_value = trigram_list[i][2]
        if tri_key in dict_list:
            dict_list[tri_key].append(tri_value)
        else:
            dict_list[tri_key] = [tri_value]

    
    for k, v in dict_list.items():
        print('Keys:',k,'\n','Values:',v)


    # print(dict_list.keys())
    # print()
    # print(dict_list.values())

 
    # print(dict_list)


    # print(l_book)
    # print()
    # print(trigram_list)

    # bigram_list = []
    # for i in range(len(l_book)-1):
    #     bigram_list.append((l_book[i],l_book[i+1]))

    # trigram_list = []
    # for i in range(len(l_book)-2):
    #     trigram_list.append((l_book[i],l_book[i+1],l_book[i+2]))

    # print(trigram_list)

    # dict_list = {}
    # for i in range(len(trigram_list)):
    #     tri_key = trigram_list[i][0] + ' ' + trigram_list[i][1]
    #     tri_value = trigram_list[i][2]
    #     dict_list[tri_key] = tri_value
    
    
    # find_key = bigram_list[0][0] + ' ' + bigram_list[0][1]
    # find_value = dict_list[find_key]

    # print(find_key,find_value)

    #print(my_trigram)


    # print(tri_key,tri_value)
    # print(dict_list)
    # print(trigram_list[0][1])
    # print(bigram_list)
    # print()
    # print(trigram_list)

trigram_fun()
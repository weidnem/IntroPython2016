'''
Write some functions that:

return a sequence with the first and last items exchanged.
return a sequence with every other item removed
return a sequence with the first and last 4 items removed, and every other item in between
return a sequence reversed (just with slicing)
return a sequence with the middle third, then last third, then the first third in the new order
'''

def first_last_exchanged():
    list = input ("Enter a sequence of any charecters:  ")
    
    return list[-1] + list[1:-1] + list[0]

first_last_exchanged()

def remove_evryothr():
    seq = input("Please enter any sequence so that all even sequence will be removed :")
    return seq[::2]

remove_evryothr()

def first_lastfourRemoved():
    seq = input("Please enter any sequence so that the first and last 4 items will be removed and every other itme in between :")
    return seq[1:-4:2]

first_lastfourRemoved

def reversed():
    seq = input("Please enter any sequence so that the sequence will be reversed! :")
    return seq[::-1]
reversed()


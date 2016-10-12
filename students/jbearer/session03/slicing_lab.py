# Slicing LAB
# October 11, 2016

def exch_func():
    l = [ '0', '1', '2', '3', '4', '5', '6', '7', '8',]
    first = l[0]
    last = l[-1]
    l[0] = last
    l[-1] = first

    print(l)
exch_func()


def skip_list():
    l = [ '0', '1', '2', '3', '4', '5', '6', '7', '8']
    new_l = l[0:len(l):2]
    print(new_l)
skip_list()

def first4_last4():
    l = [ '0', '1', '2', '3', '4', '5', '6', '7', '8',]
    new_l = l[0:4] + l[-4:]
    print(new_l)
first4_last4()

def reverse_func():
    l = [ '0', '1', '2', '3', '4', '5', '6', '7', '8']
    new_l = l[::-1]
    print(new_l)
reverse_func()

def middle3_last3():
    l = [ '0', '1', '2', '3', '4', '5', '6', '7', '8' ]
    new_l = l[3:6] + l[-3:] + l[:3]
    print(new_l)
middle3_last3()

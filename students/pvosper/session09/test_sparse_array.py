#!/usr/bin/env python3

'''
Simple testst for SparseArray
'''

from sparse_array import SparseArray

def test_len():
    sa = SparseArray([1,2,0,0,0,0,3,0,0,4])
    assert len(sa) == 10

'''
sa[5] = 12
sa[3] = 0 # the zero won't get stored!
val = sa[13] # it should get a zero if not set

del sa[4]

It should raise an IndexError if you try to access an index beyond the end.
IndexError: list index out of range
it should have an append() method
Can you make it support slicing?
How else can you make it like a list?
'''
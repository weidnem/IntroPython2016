#!/usr/bin/env python3

'''
A spare array class should present to the user the same interface as a regular
list.

Some ideas of how to do that:

Internally, it can store the values in a dict, with the index as the keys. So
that only the indexes with non-zero values will be stored.

It should take a sequence of values as an initializer:


'''

''' @chb
you should use != -- you do want to store negative numbers.
though I don't think I tested for that! -- hard to figure out everything you want to test!
'''
class SparseArray:
    def __init__(self, seq):
        self.length = len(seq)
        self.sparse_dict = {}
        ''' @chb:
        maybe enumerate here:
        for i, val in enumerate(seq):
        '''
        for i in range(len(seq)):
            if seq[i] > 0:
                self.sparse_dict[i] = seq[i]

    def __len__(self):
        return self.length
        
    def __getitem__(self, i):
        if i > self.length - 1:
            raise IndexError('list index out of range')
        elif i in self.sparse_dict.keys():
            return self.sparse_dict[i]
        else:
            return 0

    # This is crazy but works
    ''' @ CHB:
    it is an inherently ugly problem :-)
    I think it could be a bit cleaner, but I'm not seeing how right now....
    if it works, you're good to go.
    note how inefficient it is -- having to move everything around when you delete.
    '''
    def __delitem__(self, i):
        if i > self.length - 1:
            raise IndexError('list index out of range')
        elif i in self.sparse_dict.keys():
            del self.sparse_dict[i]
            for j in self.sparse_dict.keys():
                if j > i:
                    self.sparse_dict[j - 1] = self.sparse_dict[j]
                    del self.sparse_dict[j]
            self.length -= 1
        else:
            for j in self.sparse_dict.keys():
                if j > i:
                    self.sparse_dict[j - 1] = self.sparse_dict[j]
                    del self.sparse_dict[j]
            self.length -= 1
            
    def append(self, item):
        if item != 0:
            self.sparse_dict[self.length] = item
            self.length += 1
        else:
            self.length += 1              

# sa = SparseArray([7,29,0,0,0,0,13,0,0,72])
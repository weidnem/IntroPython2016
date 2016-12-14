#!/usr/bin/env python
'''
Given an array of ints, return True if 6 appears as either the first or last
element in the array. The array will be length 1 or more.
first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False
'''


def hard_six(ints):
    return ints[0] == 6 or ints[-1] == 6


if __name__ == '__main__':
    first_last6 = [1, 2, 6]
    hard_six(first_last6)

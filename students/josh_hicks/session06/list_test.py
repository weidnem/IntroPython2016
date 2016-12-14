#!/usr/bin/env python
'''
first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False
'''

from list_tdd import hard_six


def test_1():
    first_last6 = [1, 2, 6]
    assert hard_six(first_last6) is True


def test_2():
    first_last6 = [6, 1, 2, 3]
    assert hard_six(first_last6) is True


def test_3():
    first_last6 = [13, 6, 1, 2, 3]
    assert hard_six(first_last6) is False

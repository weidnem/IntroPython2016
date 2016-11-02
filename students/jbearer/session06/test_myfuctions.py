#!/usr/bin/env/python3
"""
LAB: pytest
November 1, 2016
"""

from myfunctions import monkey_trouble, squirrel_play

def test_monkey_true_true():
    assert monkey_trouble(True, True)

def test_monkey_false_false():
    assert monkey_trouble(False, False)

def test_monkey_true_false():
    assert not monkey_trouble(True, False)

def test_squirrel_play():
    assert squirrel_play(70, False) is True

def test_squirrel_play():
    assert squirrel_play(95, False) is False

def test_squirrel_play():
    assert squirrel_play(95, True) is True

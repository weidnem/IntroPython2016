#!/usr/bin/env python


def safe_input():
    try:
        sInput = input('-->')
        return sInput
    except(EOFError, KeyboardInterrupt):
        return None

if __name__ == '__main__':
    safe_input()

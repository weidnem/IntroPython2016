#!/usr/bin/env python
"""
Timing context manager
"""


import time


class Timer:

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("elapsed time:", time.time() - self.start)

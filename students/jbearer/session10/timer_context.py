#!/user/bin/env python
"""
timing context manager
"""
import sys
import time

class Timer:

    def __init__(self, outfile):
        self.outfile = outfile

    def __enter__(self):
        self.start = time.time()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('elapsed time:', time.time() - self.start)
        # self.outfile.write('elapsed time: {}'.format(ti))
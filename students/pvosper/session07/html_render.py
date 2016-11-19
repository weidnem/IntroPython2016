#!/usr/bin/env python3

'''
Given formatted input, will write out a properly formatted html file

Unit tests using PyTest:
    py.test test_html_render.py

Running tests using ipython:
    run run_html_render.py
    Creates -> test_html_output<step #>.html
'''

class Element:
    # Class attributes are shared by all instances
    tag = 'html'

    # The __init__ method gets called when memory for the object is allocated
    
    def __init__(self, content=None):
        # Instance attributes unique to each instance
        self.content = []
        if content:
            self.content.append(content)

    # Other Methods
   
    def append(self, content):
        self.content.append(content)
        
    def render(self, out_file, ind = ''):
        # out_file.write('<html>\n')
        out_file.write("<{}>\n".format(self.tag))
        for entry in self.content:
            out_file.write(entry + " ")
        # out_file.write('\n</html>')
        out_file.write("</{}>\n".format(self.tag))
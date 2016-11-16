# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 19:13:50 2016

@author: noner_000

"""

class Element:
    
    def __init__(self, content=None):
        self.content = []
        if content:
            self.content.append(content)
    
    def append(self, content):
        self.content.append(content)

    def render(self, out_file):
        out_file.write("<html>\n")
        for stuff in self.content:
            out_file.write(stuff + "\n")
        out_file.write("</html>\n")
        
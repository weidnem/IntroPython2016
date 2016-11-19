#!/usr/bin/env python3

"""
Chris's solution part way through step 2
"""


class Element:

    tag = 'html'

    def __init__(self, content=None):
        self.content = []
        if content:
            self.content.append(content)

    def append(self, content):
        self.content.append(content)

    def render(self, out_file, ind=""):
        out_file.write("<{}>\n".format(self.tag))
        for stuff in self.content:
            out_file.write(stuff + "\n")
        out_file.write("</{}>\n".format(self.tag))


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


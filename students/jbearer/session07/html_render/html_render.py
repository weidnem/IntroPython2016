#!/usr/bin/env python3


class Element:
    
    tag = 'html'
    indent = "    "

    def __init__(self, content=None):
        self.content = []
        if content:
            self.content.append(content)

    def append(self, content):
        self.content.append(content)

    def render(self, out_file, ind=''):
        out_file.write("<{}>\n".format(self.tag))
        for stuff in self.content:
            try:
                stuff.render(out_file)
            except AttributeError:
                out_file.write(str(stuff) + '\n')
        out_file.write("</{}>\n".format(self.tag))


class Html(Element):
    tag = 'html'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class Title(Element):
    tag = 'title'

# print(help(Body))





#!/usr/bin/env python

class Element:
    def __init__(self, content=None):

        tag = ''

        self.content = []
        if content:
            self.content.append(content)

    def append(self, content):
        self.content.append(content)

    def render(self, out_file, ind=''):
        if self.tag == 'html':
            out_file.write('<html>\n')
        for stuff in self.content:
            out_file.write(stuff + '\n')
        if self.tag == 'html':
            out_file.write('</html>\n')


class Html(Element):
    tag = 'html'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

#!/usr/bin/env python

class Element:
    
    tag = 'aaa'

    def __init__(self, content=None):
        self.content = []
        if content:
            self.content.append(content)

    def append(self, content):
        self.content.append(content)

    def render(self, out_file, ind=''):
        print(self.tag)
        if self.tag == 'html':
            out_file.write('<html>\n')
        for stuff in self.content:
            out_file.write(stuff + '\n')
        
        print(Body().tag)
        print(Body().content)
        if Body().tag == 'body':
            out_file.write('<body>\n')
        for stuff in Body().content:
            out_file.write(stuff + '\n')
        if Body().tag == 'body':
            out_file.write('</body>\n')
        
        if self.tag == 'html':
            out_file.write('</html>\n')



class Html(Element):
    tag = 'html'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

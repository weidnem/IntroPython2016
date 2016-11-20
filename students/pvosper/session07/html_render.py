#!/usr/bin/env python3

'''
Given formatted input, will write out a properly formatted html file

Unit tests using PyTest:
    py.test test_html_render.py

Running tests using ipython:
    run run_html_render.py
    Creates -> test_html_output<step #>.html
'''

# Chris' method:
class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        file_out.write(current_ind + self.text)

class Element:
    # Class names should normally use the CapWords convention
    # Class attributes are shared by all instances
    tag = 'element'    # Element doesn't really have a tag
    ind = ''

    # The __init__ method gets called when memory for the object is allocated
    
    def __init__(self, content=None):
        # Instance attributes unique to each instance
        self.content = []
        if content:
            self.content.append(content)
                    
    # Other Methods
   
    def append(self, content):
        if hasattr(content, 'render'):
            self.content.append(content)
        else:
            self.content.append(TextWrapper(str(content)))
        
    def render(self, out_file, ind = ''):
        # self = <html> object (assume 1)
        out_file.write(ind + '<{}>\n'.format(self.tag))
        for body in self.content:
            # body = <body> object (assume 1)
            out_file.write(ind + '<{}>\n'.format(body.tag))
            for p in body.content:
                # p = <p> objects (assume multiple)
                out_file.write(ind + '<{}>\n'.format(p.tag))
                out_file.write(ind + p.content[0] + '\n')
                out_file.write(ind + '</{}>\n'.format(p.tag))
            out_file.write(ind + '</{}>\n'.format(body.tag))
        out_file.write(ind + '</{}>\n'.format(self.tag))
        
class Html(Element):
    tag = 'html'
    ind = ''

class Body(Element):
    tag = 'body'
    ind = '    '

class P(Element):
    tag = 'p'
    ind = '        '

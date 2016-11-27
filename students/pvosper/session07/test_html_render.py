#!/usr/bin/env python3

'''
Test code for html_render.py

'''

import io

from html_render import Element, Html, Body, P, A

def test_init():
    e = Element()
    
    e = Element('this is some text')
    
def test_content():
    # fixme: this tests internals!!!!
    e = Element('this is some text')
    
    assert 'this is some text' in e.content
    
def test_append():
    e = Element('this is some text')
    
    e.append('some more text')

    assert 'some more text' in e.content
    
def test_two_instances():
    e = Element('this is some text')
    e2 = Element('this is some other text')

    e.append('some more text')
    
    assert 'some more text' not in e2.content

def test_render():
    outfile = io.StringIO()
    e = Element('this is some text')
    e.append('some more text')
    e.render(outfile)
    
    outfile.seek(0)
    file_contents = outfile.read()
    
    assert('this is some text') in file_contents
    assert('some more text') in file_contents
    
    assert file_contents.startswith('<html>')
    assert file_contents.strip().endswith('</html>')

def test_link():
    outfile = io.StringIO()
    a = A("http://google.com", "link")
    # assert '<a href="http://google.com">link</a>' == a.content

    a.render(outfile)
    
    outfile.seek(0)
    file_contents = outfile.read()
    
    print(file_contents)

    assert file_contents.startswith('<a href="')
    assert file_contents.strip().endswith('</a>')
    

# test Html, Body, P
# self.html_attr
# self.html_attr = ' '.join
# self.tag_open = '<{}{}>\n
# self.tag_open_single_line
# self.tag_close = '</{}>\n
# OneLineTag
# SelfClosingTag

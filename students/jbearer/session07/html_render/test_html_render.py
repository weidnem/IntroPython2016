#!/usr/bin/env python


"""
test code for html_render.py
"""

import io

from html_render import Element, Html, Body, P

def test_init():
    e = Element()

    e = Element('this is some text')

def test_content():
    #fixme: this tests internals!!!!
    e = Element('this is some text')

    assert 'this is some text' in e.content == ['this is some text']

def test_append():
    e = Element('this is some text')

    e.append('some more text')

    assert 'some more text' in e.content

def test_two_instances():
    e = Element('this is some text')
    e2 = Element('this is some text')

    e.append('some more text')

    assert 'some more text' not in e2.content

def test_render():
    outfile = io.StringIO()

    e = Element('this is some text')
    e.append('and this is some more text')

    e.render(outfile, '')

    outfile.seek(0)
    file_content = outfile.read()

    assert('this is some text') in file_content
    assert('and this is some more text') in file_content

    assert file_content.startswith('<html>')
    assert file_content.strip().endswith('</html>')

def test_html():
    e = Html()
    # e.append('Some text here...')
    
    with open('testfile.html', 'w') as outfile:
        e.render(outfile, '')


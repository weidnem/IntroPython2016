# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 19:04:42 2016

@author: noner_000

test code for html_render.py
"""
import io
from html_render import Element

def test_init():
    e = Element()
    
    e = Element("this is some text")
    
def test_content():
    
    e = Element("this is some text")
    
    assert "this is some text" in e.content
def test_append():
    e = Element("this is some text")
    
    e.append("some more text")
    
    assert "some more text" in e.content
    
def test_render():
    outfile = io.StringIO()
    e = Element("this is some text")
    e.append("and this is some more text")
    e.render(outfile)
    outfile.seek(0)
    file_contents = outfile.read()
    
    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<html>")
    assert file_contents.strip().endswith("</html>")
"""
Name: Paul Briant
Date: 11/15/16
Class: Introduction to Python
Session: 07
Assignment: HTML Renderer

Description:
Tests for HTML Renderer
"""

# -------------------------------Imports----------------------------------------
from html_renderer import Element
import io

# -------------------------------Functions--------------------------------------


def test_init():
    e = Element()
    e = Element("Please remain calm, this is a test.")


def test_content():
    """
    Checks whether content is a str.
    """
    e = Element("Testing 1 2 3..")
    assert type(e.content) is str
    assert "Testing 1 2 3.." in e.content


def test_append():
    """
    Verifies additional content is successfully added to rest of content
    """


def test_render():
    """
    Tests whether render successfully writes content to file by creating
    instance of element, adding content to it using the append function and
    calling the render funtion on it.
    """
    # Creates in memory version of content to write to file
    output = io.StringIO()
    e = Element("Hello World!")
    e.append("Wazzup World!")
    e.render(output)

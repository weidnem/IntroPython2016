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
import html_renderer
import io

# -------------------------------Functions--------------------------------------


def test_content():
    """
    Checks whether content is a str.
    """
    assert type(self.content) is str


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
    e = html_renderer.Element("Hello World!")
    e.append("Wazzup World!")
    e.render(output)

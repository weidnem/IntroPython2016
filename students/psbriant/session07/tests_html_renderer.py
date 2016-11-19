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
    assert type() is str


def test_append():
    """
    Verifies additional content is successfully added to rest of content
    """


def test_render():
    """

    """
    output = io.StringIO()
    e = html_renderer.Element("Hello World!")
    e.render(output)

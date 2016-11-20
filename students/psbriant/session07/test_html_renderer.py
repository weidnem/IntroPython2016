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
from html_renderer import Element, Html, Body, P
import io

# -------------------------------Functions--------------------------------------


def test_init():
    e = Element()
    e = Element("Please remain calm, this is a test.")


def test_content():
    """
    Checks whether content is a str.

    Question:
    Ask about why type based testcase fails.
    """
    e = Element("Testing, 1 2 3..")
    assert "Testing, 1 2 3.." in e.content


def test_append():
    """
    Verifies additional content is successfully added to rest of content
    """
    e = Element("Please remain calm, this is a test.")
    e.append("DON'T PANIC!")
    assert "DON'T PANIC!" in e.content


def test_two_instances():
    e = Element("Testing, 1 2 3..")
    e2 = Element("Testing, 1 2 3..")
    e.append("More tests! We need more tests!")
    assert "More tests! We need more tests!" not in e2.content


def test_render():
    """
    Tests whether render successfully writes content to file by creating
    instance of element, adding content to it using the append function and
    calling the render funtion on it.
    """
    # Creates in memory version of content to write to file
    output = io.StringIO()
    e = Element("Testing, 1 2 3..")
    e.append("DON'T PANIC")
    e.render(output, "")
    file_cont = output.getvalue()
    assert("Testing, 1 2 3..") in file_cont
    assert("DON'T PANIC") in file_cont
    assert file_cont.startswith("<html>")
    assert file_cont.strip().endswith("</html>")


def test_html_render():
    """
    Tests whether render successfully writes content to file for the html tag
    by creating instance of element, adding content to it using the append
    function and calling the render funtion on it.
    """
    # Creates in memory version of content to write to file
    output = io.StringIO()
    e = Html("Testing, 1 2 3..")
    e.append("DON'T PANIC")
    e.render(output, "")
    file_cont = output.getvalue()
    assert file_cont.startswith("<html>")
    assert file_cont.strip().endswith("</html>")


def test_body_render():
    """
    Tests whether render successfully writes content to file for the body tag
    by creating instance of element, adding content to it using the append
    function and calling the render funtion on it.
    """
    # Creates in memory version of content to write to file
    output = io.StringIO()
    e = Body("Testing, 1 2 3..")
    e.append("DON'T PANIC")
    e.render(output, "")
    file_cont = output.getvalue()
    assert file_cont.startswith("<body>")
    assert file_cont.strip().endswith("</body>")


def test_p_render():
    """
    Tests whether render successfully writes content to file for the p tag
    by creating instance of element, adding content to it using the append
    function and calling the render funtion on it.
    """
    # Creates in memory version of content to write to file
    output = io.StringIO()
    e = P("Testing, 1 2 3..")
    e.append("DON'T PANIC")
    e.render(output, "")
    file_cont = output.getvalue()
    assert file_cont.startswith("<p>")
    assert file_cont.strip().endswith("</p>")

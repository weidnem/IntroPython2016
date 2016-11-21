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
import html_render as hr
import io

# -------------------------------Functions--------------------------------------


def test_init():
    e = hr.Element()
    e = hr.Element("Please remain calm, this is a test.")


def test_content():
    """
    Checks whether content is a str.
    """
    e = hr.Element("Testing, 1 2 3..")
    assert "Testing, 1 2 3.." in e.content


def test_append():
    """
    Verifies additional content is successfully added to rest of content
    """
    e = hr.Element("Please remain calm, this is a test.")
    e.append("DON'T PANIC!")
    assert "DON'T PANIC!" in e.content


def test_two_instances():
    e = hr.Element("Testing, 1 2 3..")
    e2 = hr.Element("Testing, 1 2 3..")
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
    e = hr.Element("Testing, 1 2 3..")
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
    e = hr.Html("Testing, 1 2 3..")
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
    e = hr.Body("Testing, 1 2 3..")
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
    e = hr.P("Testing, 1 2 3..")
    e.append("DON'T PANIC")
    e.render(output, "")
    file_cont = output.getvalue()
    assert file_cont.startswith("<p>")
    assert file_cont.strip().endswith("</p>")


def test_append_instances():
    """
    Test to verify an instance of an html element can be appended into another.
    """
    output = io.StringIO()
    e_body = hr.Body()
    e_p = hr.P("Testing, 1 2 3..")
    e_body.append(e_p)
    e_body.render(output, "")
    file_cont = output.getvalue()
    assert file_cont.startswith("<body>")
    assert file_cont.strip().endswith("</body>")
    print(file_cont)
    assert "Testing, 1 2 3.." in file_cont
    # check p tag is in body
    assert "<p>" in file_cont and "</p>" in file_cont
    # additional tests?


def test_head_render():
    """
    Tests whether render successfully writes content to file for the head tag
    by creating instance of element, adding content to it using the append
    function and calling the render funtion on it.
    """
    output = io.StringIO()
    e = hr.Head("Testing, 1 2 3..")
    e.append("DON'T PANIC")
    e.render(output, "")
    file_cont = output.getvalue()
    assert file_cont.startswith("<head>")
    assert file_cont.strip().endswith("</head>")


def test_onelinetag_title():
    """
    Tests whether the element subclass of onelinetag successfully writes all
    content on the same line to  a file for the inline tag 'title'. This is
    tested by creating an instance of title, adding content to it using the
    append function and calling the render funtion on it.
    """
    output = io.StringIO()
    e = hr.Title("Testing, 1 2 3..")
    e.append("DON'T PANIC")
    e.render(output, "")
    file_cont = output.getvalue()
    assert "\n" not in file_cont
    assert file_cont.startswith("<title>")
    assert file_cont.strip().endswith("</title>")

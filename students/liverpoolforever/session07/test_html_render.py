''' will test html_render.py '''

# import pytest

from html_render import Element,Wrong_Element,Html,Body

def test_init():
	# e = Element()
	e = Element("foo")


def test_txt():
	''' test if content is passed'''
	ANS = "foo"
	ANS1 = "bar"
	e = Wrong_Element("foo")
	e1 = Wrong_Element("bar")
	result = e.get_txt()
	result1 = e1.get_txt()
	assert result1 is ANS1
	assert result is ANS

def test_content():
	''' test the content list '''
	ANS = 1
	e = Element("foo")
	e1 = Element("bar")

	result = e.get_content()
	assert result is ANS

def test_append():
	'''test append method'''
	ANS = 2
	e = Element("foo")
	e.append("bar")

	result = e.get_content()
	assert result is ANS

def test_render():
	e = Element("Some text")
	e.append("More text")
	with open("test1.html",'w') as outfile:
		e.render(outfile)

def test_html_render():
	html_obj = Html("Some html text")
	html_obj.append("more html text")

	body_obj = Body("I am a body element")

	with open("test3.html","w") as outfile:
		body_obj.render(outfile)

	with open("test2.html","w") as outfile:
		html_obj.render(outfile)






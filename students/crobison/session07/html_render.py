#!/usr/bin/env python3


class TextWrapper:
    """
    Copied from solution.
    Creates a class with a render method
    just for text
    Allows the Element classes to render either Element
    objects or plain text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind = ""):
        file_out.write(current_ind + self.text)


class Element:
    tag = "html"
    indent = "    "

    def __init__(self, content=None):
        self.content = []
        if content is not None:
            self.content.append(content)

    def append(self, content):
        if hasattr(content, 'render'):
            self.content.append(content)
        else:
            self.content.append(TextWrapper(str(content)))

    def render(self, out_file, ind=""):
        out_file.write("<{}>\n".format(ind, self.tag))
        for stuff in self.content:
            stuff.render(out_file, ind + self.indent)
            out_file.write("\n")
        out_file.write("</{}>\n".format(ind, self.tag))

class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"






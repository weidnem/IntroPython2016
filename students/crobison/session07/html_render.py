#!/usr/bin/env python3

<<<<<<< HEAD

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
=======
class Element:
    def __init__(self, content=None):
        self.content = []
        self.tag = "html"
>>>>>>> a65f03242cb651da1986af22477ff12ea19b4c8a
        if content is not None:
            self.content.append(content)

    def append(self, content):
<<<<<<< HEAD
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
=======
        self.content.append(content)

    def render(self, out_file, indent=""):
        out_file.write("<{}>\n".format(self.tag))
        for stuff in self.content:
            try:
                new_ind = indent + "    "
                stuff.render(out_file, indent=new_ind)
                out_file.write("\n")
            except AttributeError:
                out_file.write(new_ind + str(stuff) + "\n")
        out_file.write("</{}>\n".format(self.tag))

    # def render(self, out_file, indent=""):
    #     out_file.write("<{}>\n".format(self.tag))
    #     for stuff in self.content:
    #         new_ind = indent + "    "
    #         if self.tag == "p":
    #             stuff.render(out_file, indent=new_ind)
    #             out_file.write("\n")
    #         if self.tag == "body":
    #             new_ind = indent + "    "
    #             stuff.render(out_file, indent=new_ind)
    #             out_file.write("\n")
    #         if self.tag == "html":
    #             out_file.write(new_ind + str(stuff) + "\n")
    #     out_file.write("</{}>\n".format(self.tag))
>>>>>>> a65f03242cb651da1986af22477ff12ea19b4c8a

class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

<<<<<<< HEAD

=======
class Head(Element):
    tag = "head"

class OneLineTag(Element):
    
>>>>>>> a65f03242cb651da1986af22477ff12ea19b4c8a




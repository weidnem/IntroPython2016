#!/usr/bin/env python3

class Element:
    tag = "html"
    def __init__(self, content="", ind=""):
        self.ind = ind
        self.content = []
        if content:
            self.content.append(content)


    def append(self, content):
        self.content.append(content)

    def render(self, out_file, ind=""):
        out_file.write("{}<{}>\n".format(ind, self.tag))
        for item in self.content:
            try:
                new_ind = ind + "    "
                item.render(out_file, ind=new_ind)
                out_file.write("\n")
            except AttributeError:
                out_file.write(new_ind + str(item) + "\n")
        out_file.write("{}</{}>".format(ind, self.tag))


class Head(Element):
    tag = "head"


class Html(Element):
    tag = "html"


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class OneLineTag(Element):
    def render(self, out_file, ind=""):
        out_file.write("{}<{}>".format(ind, self.tag) + str(self.content[0]) + "</{}>".format(self.tag))


class Title(OneLineTag):
    tag = "title"

#!/usr/bin/env python3

class Element:
    tag = "html"
    def __init__(self, content="", **kwargs):
        self.content = []
        self.attributes = []
        if content:
            self.content.append(content)
        for k in kwargs:
            # think about using ordered dict
            self.attributes.append((k, kwargs[k]))


    def append(self, content):
        self.content.append(content)


    def render_opening_tag(self):
        attr = ""
        for x, y in self.attributes:
            attr += " "
            attr += "{}=\"{}\"".format(x, y)
        return attr


    def render(self, out_file, ind=""):
        out_file.write("{}<{}{}>\n".format(ind, self.tag, self.render_opening_tag()))
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
        out_file.write("{}<{}{}>".format(ind, self.tag, self.render_opening_tag()) + str(self.content[0]) + "</{}>".format(self.tag))


class Title(OneLineTag):
    tag = "title"


class A(OneLineTag):
    tag = "a"
    def __init__(self, link, content, **kwargs):
        kwargs["href"] = link
        super().__init__(content, **kwargs)


class SelfClosingTag(Element):
    def render(self, out_file, ind=""):
        out_file.write("{}<{}{} />".format(ind, self.tag, self.render_opening_tag()))


class Br(SelfClosingTag):
    tag = "br"


class Hr(SelfClosingTag):
    tag = "hr"


class Img(SelfClosingTag):
    tag = "img"

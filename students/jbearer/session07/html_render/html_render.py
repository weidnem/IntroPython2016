#!/usr/bin/env python3



class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for just text
    This allows the Element classes to render either Element objects or
    plain text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        file_out.write(current_ind + self.text)

class Element:
    
    tag = 'html'
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.content = []
        if content:
            self.append(content)

    def append(self, content):
        if hasattr(content, 'render'):
            self.content.append(content)
        else:
            self.content.append(TextWrapper(str(content)))

    def render(self, out_file, ind=''):
        open_tag, close_tag = self.make_tags()
        out_file.write(ind + open_tag + '\n')
        for stuff in self.content:
            stuff.render(out_file, ind + self.indent)
            out_file.write('\n')
        out_file.write(ind + close_tag)


   
    def make_tags(self):
        """
        create the tags
        -- in a separate method so different subclass's render methods can use it
        """
        attrs = " ".join(['{}="{}"'.format(key, val) for key, val in self.attributes.items()])
        if attrs.strip():
            open_tag = "<{} {}>".format(self.tag, attrs.strip())
        else:
            open_tag = "<{}>".format(self.tag)
        close_tag = "</{}>".format(self.tag)

        return open_tag, close_tag

class OneLineTag(Element):
    # note: by re-writting the render
    def render(self, out_file, ind=""):
        # there is some repition here -- maybe factor that out?
        open_tag, close_tag = self.make_tags()
        out_file.write(ind + open_tag)
        for stuff in self.content:
            stuff.render(out_file)
        out_file.write(close_tag)

class Html(Element):
    tag = 'html'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class Title(OneLineTag):
    tag = 'title'

class SelfClosingTag(Element):
    """
    base class for tags that have no content
    """
    def render(self, out_file, ind=""):
        # there is some repition here -- maybe factor that out?
        open_tag, _ = self.make_tags()
        # make it a self cloding tag by adding the /
        out_file.write(ind + open_tag.replace(">", " />"))

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class A(OneLineTag):
    """
    anchor element
    """
    tag = "a"

    def __init__(self, link, content, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)
        # this could also be direct:
        # Element.__init__(self, content, **kwargs)

class Ul(Element):
    """
    unordered list
    """
    tag = "ul"


class Li(Element):
    """
    list element
    """
    tag = "li"


class H(OneLineTag):
    """
    section head
    """
    tag = "H"

    def __init__(self, level, content=None, **kwargs):
        self.tag = "h" + str(int(level))
        super().__init__(content, **kwargs)


# print(help(Body))





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

class Title(Element):
    tag = 'title'

# print(help(Body))





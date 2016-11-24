"""
Name: Paul Briant
Date: 11/22/16
Class: Introduction to Python
Session07
LAB: HTML Renderer

Description:

"""
# -------------------------------Imports----------------------------------------


# -------------------------------Classes--------------------------------------
class Element:

    tag = 'html'
    num_ind = 0

    def __init__(self, content=None, **kwargs):
        """
        Initializes class attribute content and appends any value not equal to
        none into and empty list.
        """
        self.attributes = kwargs
        self.content = []
        if content:
            self.content.append(content)

    def append(self, content):
        """
        Takes in new content in the form of a string and adds it to list of
        existing content.
        """
        self.content.append(content)

    def make_tags(self):
        """
        Generalizes the creation of tags and allows for tags to be created with
        or without attributes.
        """
        attrs = " ".join(['{}="{}"'.format(key, val) for key, val in self.attributes.items()])
        if attrs.strip():
            open_tag = "<{} {}>".format(self.tag, attrs.strip())
        else:
            open_tag = "<{}>".format(self.tag)
        close_tag = "</{}>".format(self.tag)

        return open_tag, close_tag

    def render(self, file_out, ind=""):
        """
        Takes in the output file, generates opening and closing tags and
        inserts each individual line of content in between it. All tags and
        content are written to output file.
        """
        open_tag, close_tag = self.make_tags()
        file_out.write((ind * self.num_ind) + open_tag + "\n")
        for stuff in self.content:
            stuff.render(file_out, (ind * self.num_ind) + self.indent)
            file_out.write("\n")
        file_out.write(ind + close_tag)


class Html(Element):
    tag = 'html'
    num_ind = 0


class Body(Element):
    tag = 'body'
    num_ind = 1


class P(Element):
    tag = 'p'
    num_ind = 2


class Head(Element):
    tag = 'head'
    num_ind = 1


class OneLineTag(Element):
    def render(self, file_out, ind=""):
        """
        Takes in the output file, generates opening and closing tags and
        inserts each individual line of content in between it. All tags and
        content are written to output file.
        """
        file_out.write("{}<{}>{}</{}>\n".format((ind * self.num_ind), self.tag,
                       " ".join(self.content), self.tag))


class Title(OneLineTag):
    tag = 'title'
    num_ind = 2


class SelfClosingTag(Element):
    def render(self, file_out, ind=""):
        """
        Take in an output file and generate a self closing tag.
        """
        file_out.write("{}<{} />\n".format((ind * self.num_ind), self.tag))


class Hr(SelfClosingTag):
    tag = 'hr'
    num_ind = 2


class Br(SelfClosingTag):
    tag = 'br'
    num_ind = 3

# ==============================================================================


def main():
    """
    Calls functions and produces output.
    """


if __name__ == '__main__':
    main()

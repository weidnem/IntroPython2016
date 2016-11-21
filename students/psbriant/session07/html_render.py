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

    def __init__(self, content=None):
        """
        Initializes class attribute content and appends any value not equal to
        none into and empty list.
        """
        self.content = []
        if content:
            self.content.append(content)

    def append(self, content):
        """
        Takes in new content in the form of a string and adds it to list of
        existing content.
        """
        self.content.append(content)

    def render(self, file_out, ind=""):
        """
        Takes in the output file, generates opening and closing tags and
        inserts each individual line of content in between it. All tags and
        content are written to output file.
        """
        file_out.write("{}<{}>\n".format((ind * self.num_ind), self.tag))
        for stuff in self.content:
            try:
                stuff.render(file_out, ind)
            except AttributeError:
                file_out.write((3*ind)+stuff+"\n")
        file_out.write("{}</{}>\n".format(ind * self.num_ind, self.tag))


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


# ==============================================================================


def main():
    """
    Calls functions and produces output.
    """


if __name__ == '__main__':
    main()

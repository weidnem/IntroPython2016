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
        file_out.write("<{}>\n".format(self.tag))
        for stuff in self.content:
            try:
                stuff.render(file_out, ind)
            except AttributeError:
                file_out.write(stuff+"\n")
        file_out.write("</{}>\n".format(self.tag))


class Html(Element):
        tag = 'html'


class Body(Element):
        tag = 'body'


class P(Element):
        tag = 'p'


# ==============================================================================


def main():
    """
    Calls functions and produces output.
    """


if __name__ == '__main__':
    main()

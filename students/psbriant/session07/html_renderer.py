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

        """
        self.content.append(content)

    def render(self, file_out):
        """

        """
        file_out.write("<{}>\n".format(self.tag))
        for stuff in self.content:
            file_out.write(stuff+"\n")
        file_out.write("</{}>\n".format(self.tag))


# ==============================================================================


def main():
    """
    Calls functions and produces output.
    """


if __name__ == '__main__':
    main()

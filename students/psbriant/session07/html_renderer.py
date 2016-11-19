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
class Element(content=None):
    def __init__(self, tag, indent):
        """
        Initializes class attributes tag and spaces.
        """
        self.tag = tag
        self.spaces = indent

    def append(content):
        """

        """

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

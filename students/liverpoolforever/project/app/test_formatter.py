''' Test class to test formatter.py '''


from .formatter import Formatter


def test_formatter():
    ANS = "foo"
    @Formatter('json')
    def return_a_string(string):
        return string

    assert return_a_string("foo") == ANS
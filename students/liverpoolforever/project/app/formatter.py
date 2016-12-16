''' A class which formats the response from MongoDB '''

import json

#---------------------- Formatted Response Object ----------------------

class Formatter():

    def __init__(self,format_type):
        self.format_type = format_type

    def __call__(self,orig_func):
        def func(*args,**kwargs):
            string = orig_func(*args,**kwargs)
            if self.format_type == "json":
                res = "<json>{}</json>".format(string)
            else:
                res = "<{}>{}</{}>".format(self.format_type,string,self.format_type)
            return res
        return func


def test_formatter():
    @Formatter('xml')
    def return_a_string(string):
        return string
    res = return_a_string("foo")
    print(res)

if __name__ == '__main__':
    test_formatter()


        

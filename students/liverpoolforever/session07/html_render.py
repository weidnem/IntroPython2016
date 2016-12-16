''' Session07 lab - run_html_render.py'''


class Wrong_Element:
	tag_name = 'html'
	indent_no = 4

	current_txt = '' 
	# Cannot declare a list attribute as every instance of Element class will use the same list
	content = []


 # non-default argument cannot follow a default argument
	def __init__(self,text,indent=4):
		self.indent_no = indent
		if text is not None:
			self.current_txt = text
			self.content.append(text)

	def render(file_out, ind = ""):
		''' takes in a IO object to write to file'''
		for stuff in self.content:
			file_out.write(stuff)

	def append(self,text):
		'''Adds text to class attribute list'''
		self.content.append(text)

	def get_txt(self):
		'''returns curret txt of Element'''
		return self.current_txt

	def get_content(self):
		'''returns lenght of items in content list'''
		print(self.content)
		return len(self.content)


class Element:
	''' An element class generating text for html'''
	tag = 'default'
	indent_no = 4
	open_arrow = '<'
	close_arrow = '>'
	close_slash = '/'

	def __init__(self,content=None):
		self.content = []
		if content:
			self.content.append(content)

	def append(self,content):
		self.content.append(content)

	def render(self,out_file):
		open_tag = "{}{}{}".format(self.open_arrow,self.tag,self.close_arrow) 
		out_file.write(open_tag)
		for stuff in self.content:
			out_file.write(stuff + "\n")
		close_tag = "{}{}{}{}".format(self.open_arrow,self.close_slash,self.tag,self.close_arrow)
		out_file.write(close_tag)

	def get_content(self):
		return len(self.content)


class Html(Element):
	''' A sub-class of Element for HTML tags'''
	# Override only the tag attribute
	tag = 'html'
    

class Body(Element):
	''' A sub-class of Element for Body tags'''
	tag = 'body'


class P(Element):
	''' A sub-class of Element for P tags'''
	tag = 'p'

class OneLineTag(Element):
	''' A sub-class of Element to override render method'''

class Head(Element):
	'''




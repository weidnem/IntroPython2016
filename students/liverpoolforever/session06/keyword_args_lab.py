''' keyword_args lab '''

def f(x, y, w=0, h=0):	
	'''
	A practise function from session06 for testing agrs and kwargs
	'''
	print("position: {}, {} -- shape: {}, {}".format(x, y, w, h))
    

def args_params_regular(link_color='red', back_color='blue',fore_color='green',visited_color='yellow'):
	''' a method which takes 4 parameters are colors'''
	ouput_str = "link_color: {} , back_color: {} ,fore_color: {} ,visted_color: {} ".format(link_color,back_color,fore_color,visited_color)
	print(ouput_str)
	return ouput_str


def args_params_generic(*args,**kwargs):
	# ouput_str = "link_color: {} , back_color: {} ,fore_color: {} ,visted_color: {} ".format(args)
	print(args,kwargs)
	return args,kwargs
	# print(ouput_str)

def main():
	regular = ('x', 'y')
	links = {'link_color': 'chartreuse'}
	# args_params_regular('purple', link_color='red', back_color='blue')
	args_params_generic('purple', link_color='red', back_color='blue')
	# args_params_generic(*regular, **links)
	# pos_args = (1,2)
	# key_args = { 'a' : 1, 'b': 2}
	# f(pos_args,1)


if __name__ == '__main__':
	main()
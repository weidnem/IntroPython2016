''' Unit test for args_kwargs_lab.py '''

import pytest

from keyword_args_lab import args_params_generic,args_params_regular

def test_pos_args():
	result = args_params_regular('red', 'blue', 'yellow', 'chartreuse')
	print(result)
	result = args_params_generic('red', 'blue', 'yellow', 'chartreuse')
	print(result)

# def test_keyword_args():
# 	result = args_params_regular(link_color='red', back_color='blue')
# 	result = args_params_generic(link_color='red', back_color='blue')

# def test_pos_keyword():
# 	result = args_params_regular('purple', link_color='red', back_color='blue')
# 	result = args_params_generic('purple', link_color='red', back_color='blue')

# def test_generic():
# 	regular = ('x', 'y')
# 	links = {'link_color': 'chartreuse'}
# 	result = args_params_regular(*regular,**links)
# 	result = args_params_generic(*regular,**links)
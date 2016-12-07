''' Unit test for count_evens lab '''

#  from count_evens module import count_events method
from count_evens import count_evens

# checks the count only
def test_1():
	ANS = 3
	res = count_evens([2,1,2,4])
	assert res is ANS


# check string input
def test_2():
	ANS = None
	input = ['2','1','2']
	res = count_evens(input)
	assert res is ANS



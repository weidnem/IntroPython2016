''' count_evens lab from codingbat '''


# counts the even no's in a list
def count_evens(nums):

	count = 0

	for num in nums:
		# num % 2 returns 0 and 1 , and 1 is not True
		try:
			if num % 2 == 0:
				count += 1
		except TypeError as e:
			print("TypeError  {0}".format(e))
			return None
	return count

#  main method
def main():
	input_list = [2, 1, 2, 3, 4, 5,4]
	no_of_evens = count_evens(input_list)
	print("The even nums in the list are " , no_of_evens)


#  calls the main method
if __name__ == '__main__':
	main()
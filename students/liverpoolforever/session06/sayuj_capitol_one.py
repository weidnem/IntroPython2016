''' test program for capital one '''

# wrapper function for handling exceptions in inputs
def safe_input():
    try:
        response = input("==> ").strip()
        return response
    except (EOFError,KeyboardInterrupt) as e: 
        print("Input interrupted by user or end of line reached")
        return None


def count_unique():
	# get input string
	res = safe_input()
	# use a set to store unique words
	unqiue_words = set()
	words = res.split(',')
	print("Before unique count: " , words)
	for word in words:
		unqiue_words.add(word.lower())
		# print(word)

	print("unique words are " , unqiue_words)

	# pass

def main():

    response = ''
    # keep asking until the users responds with an 'x'
    while True:  # make sure there is a break if you have infinite loop!
        # print(msg)
        response = safe_input()  # strip() in case there are any spaces at the start or end
        if response == 'p':
            count_unique()
            break
        elif response == None:
            continue
        elif response == 'x':
            break
        else:
            print('please type "p" to count unique words, or "x" to quit')


if __name__ == "__main__":
    main()
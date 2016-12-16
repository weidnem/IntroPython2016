"""
The input() function can generate two exceptions: EOFError or KeyboardInterrupt on end-of-file(EOF) or canceled input.

Create a wrapper function, perhaps safe_input() that returns None rather rather than raising these exceptions, when the
user enters ^C for Keyboard Interrupt, or ^D (^Z on Windows) for End Of File.
"""

def safe_input(words):
    """
    To sanitize the input
    :param input: Input should be a string.
    :return: Exceptions if program is interrupted, otherwise passes input.
    """
    try:
        user_input = input(words)
        return user_input
    except (EOFError, KeyboardInterrupt):
        return None


if __name__ == "__main__":
    user_input = safe_input("Tell me a story: ")
    if user_input  is None:
        print("Don't be a quitter!")
    else:
        print("Thanks for playing, this is what you typed: {}".format(user_input))




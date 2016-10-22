#!/usr/bin/env python3

import random

# text_string = '''
# Trigram analysis is very simple. Look at each set of three adjacent words in a 
# document. Use the first two words of the set as a key, and remember the fact 
# that the third word followed that key. Once you’ve finished, you know the list 
# of individual words that can follow each two word sequence in the document. 
# '''

temp_file = open('sherlock_partial.txt')
text_string = temp_file.read()
temp_file.close()

text_list = text_string.split()

# Strip punctuation ,. (but not apostrophe '?)
for i, entry in enumerate(text_list):
    temp_string = ''
    for char in entry:
        if char.isalpha():
            temp_string = temp_string + char #.lower()
    text_list[i] = temp_string

# In trigrams dictionary, each value is a list of lists
trigrams = {}

# Build dictionary of trigrams
for i in range(len(text_list)-2):
    # I could make this one line, but then I would understand it even less
    key = text_list[i] + " " + text_list[i+1]
    val = [text_list[i+2]]
    trigrams.setdefault(key, []).append(val)

# seed = random.randint(0, len(trigrams))
# print(trigrams[seed])
print(random.choice(list(trigrams.keys())))

if __name__ == '__main__':
    print('\n=== MAIN ===')
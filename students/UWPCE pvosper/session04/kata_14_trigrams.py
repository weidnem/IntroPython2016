#!/usr/bin/env python3

'''
Generate text based on trigrams within a source file.
'''

import random

sentance = ""
sentance_list = []

# text_string = '''
# Trigram analysis is very simple. Look at each set of three adjacent words in a 
# document. Use the first two words of the set as a key, and remember the fact 
# that the third word followed that key. Once you’ve finished, you know the list 
# of individual words that can follow each two word sequence in the document. 
# '''

# Read in file
temp_file = open('sherlock_partial.txt')
text_string = temp_file.read().replace('\n', ' ')
temp_file.close()

# This is crude
text_string = text_string.lower()
text_string = text_string.replace('"', '')
text_string = text_string.replace(',', '')
text_string = text_string.replace('.', '')
text_string = text_string.replace('?', '')
text_string = text_string.replace('-', '')
text_string = text_string.replace(':', '')
text_string = text_string.replace(';', '')
text_string = text_string.replace("'", '')
text_string = text_string.replace('  ', ' ')
text_string = text_string.replace(' i ', ' I ')
text_string = text_string.replace(' holmes ', ' Holmes ')

# Create list
text_list = text_string.split()

# Strip punctuation ,. (but not apostrophe '?)
# . , " ? <double space>
# for i, entry in enumerate(text_list):
#     temp_string = ''
#     for char in entry:
#         if char.isalpha():
#             temp_string = temp_string + char.lower()
#     text_list[i] = temp_string

# In trigrams dictionary, each value is a list of lists
trigrams = {}

# Build dictionary of trigrams
for i in range(len(text_list)-2):
    # I could make this one line, but then I would understand it even less
    key = text_list[i] + " " + text_list[i+1]
    val = [text_list[i+2]]
    trigrams.setdefault(key, []).append(val)

def pick_value(val_list):
    # random includes upper range value
    return val_list[random.randint(0, len(val_list) - 1)]
    
def make_sentance():
    sentance = ""
    seed = random.choice(list(trigrams.keys()))
    sentance_list = seed.split()
    for i in range(random.randint(8, 72)):
        seed = sentance_list[-2] + " " + sentance_list[-1]
        sentance_list.append(pick_value(trigrams[seed])[0])
    for word in sentance_list:
        sentance = sentance + " " + word
    sentance = sentance[1].upper() + sentance[2:] + '.'
    print(sentance)
    return sentance

if __name__ == '__main__':
    print('\n=== MAIN ===\n')
    
    make_sentance()

# While true until lookup failer; then end sentence and start another
# Create list of capitalized works - from capitals mid-sentence
# I
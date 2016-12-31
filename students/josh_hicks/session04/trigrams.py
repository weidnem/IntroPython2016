#!/usr/bin/env python

import random
import string


def read_file(file):
    read_data = []
    with open(file, 'r') as f:
        for line in f:
            read_data.append(line)
    f.closed
    return read_data


def sanitize_input(trigramList):
    translator = str.maketrans({key: None for key in string.punctuation})
    for i in range(len(trigramList)):
        trigramList[i] = trigramList[i].translate(translator)
        trigramList[i] = trigramList[i].replace('\n', '')
    return trigramList


def create_trigrams_dictionary(inputFile):
    trigramList = read_file(inputFile)
    trigramListNoPunct = sanitize_input(trigramList)
    trigramDict = {}
    for i in range(len(trigramListNoPunct)):
        trigramLine = trigramListNoPunct[i].split(' ')
        for i in range(len(trigramLine)):
            currWord = trigramLine[i]
            try:
                nextWord = trigramLine[i+1]
                lastWord = trigramLine[i+2]
            except IndexError:
                break
            key = '{0} {1}'.format(currWord, nextWord)
            if key not in trigramDict:
                trigramDict.setdefault(key, [lastWord])
            else:
                trigramDict[key].append(lastWord)
    return trigramDict


def create_trigram(trigramDict):
    story = []
    for i in range(len(trigramDict)):
        wordPair = random.choice(list(trigramDict.keys()))
        nextWord = random.choice(trigramDict[wordPair])
        if i % 10 == 0:
            story.append('{0} {1}.'.format(wordPair, nextWord))
        else:
            story.append('{0} {1}'.format(wordPair, nextWord))
    return story


if __name__ == '__main__':
    trigramDict = create_trigrams_dictionary('sherlock_small.txt')
    story = create_trigram(trigramDict)
    for line in story:
        print('{0} {1}'.format(line, ' '), end='')

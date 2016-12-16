"""string formatting lab Authored by Adam Hollis"""

def formatter(tuple):
    tlen = len(tuple)
    phrase = 'the {length} numbers are: '
    for item in tuple:
        if tuple.index(item) == tlen - 1:
            phrase += '{:d}'
        else:
            phrase += '{:d}, '


    print(phrase.format(length = tlen, *tuple))

if __name__ == "__main__":
    t1 = (6, 8, 1, 5, 5, 7)
    formatter(t1)





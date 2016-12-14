#!/usr/bin/env python


if __name__ == '__main__':
    dictionary = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
    print(dictionary)
    del dictionary['cake']
    print(dictionary)
    dictionary.setdefault('fruit', 'Mango')
    for k, v in dictionary.items():
        print(k)
        print(v)
    print('cake' in dictionary)
    print('Mango' in dictionary.values())

    dictionary2 = dictionary.copy()
    for k, v in dictionary.items():
        dictionary2[k] = 't' * v.count('t')
    print(dictionary2)

    s2 = set()
    s3 = set()
    s4 = set()
    for x in range(0, 21):
        if x % 2 == 0:
            s2.add(x)
        if x % 3 == 0:
            s3.add(x)
        if x % 4 == 0:
            s4.add(x)
    print(s2)
    print(s3)
    print(s4)
    print(s3.issubset(s2))
    print(s4.issubset(s2))

    s5 = set(['p', 'y', 't', 'h', 'o', 'n'])
    s4.add('i')
    fs = frozenset(('m', 'a', 'r', 'a', 't', 'h', 'o', 'n'))
    print(fs.union(s5))
    print(fs.intersection(s5))

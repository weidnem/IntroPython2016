
def isithere(d):


    #first method to test for inclusion
    try:
        d1['cake']

    except KeyError:
        print('No cake for you!')

    #second method to test for inclusion
    if 'cake' in d1:
        print('CAKE!')
    else:
        print('NO CAKE FOR YOU!')

    #method 2 at work for values
    if 'mango' in d1.values():
        print('Mango!')
    else:
        print('No Mango!')


if __name__ == "__main__":

    d = {'name': 'Chris',
         'city': 'Seattle',
         'cake': 'Chocolate',
    }

    d1 = d.copy()
    print(d1)
    d1.pop('cake')
    print(d1)
    d1['fruit'] = 'mango'
    print(d1)

    print(d1.keys())

    print(d1.values())
    print(d)
    print(d1)

    isithere(d)






def list_comp():
    
    feast = ['lambs', 'sloths', 'orangutans','breakfast cereals', 'fruit bats']

    comprehension = [delicacy.capitalize() for delicacy in feast]

    print('comprehension:', comprehension)

    comp = [delicacy for delicacy in feast if len(delicacy) > 6]

    print('len of feast:', len(feast))
    print('len of comp:', len(comp))

# list_comp()

def tuples_comp():

    list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]

    comprehension = [skit * number for number, skit in list_of_tuples]

    print('comprehension:', comprehension[0])
    print('len of comprehension:', len(comprehension[2]))

# tuples_comp()

def double_list_comp():
    
    eggs = ['poached egg', 'fried egg']
    meats = ['lite spam', 'ham spam', 'fried spam']
    comprehension = ['{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]

    print('len of comprehension:',len(comprehension))
    print('comprehension[0]',comprehension[0])

# double_list_comp()

def set_comp():
    comprehension = { x for x in 'aabbbcccc'}
    print(comprehension)

# set_comp()

def dict_comp():
    dict_of_weapons = {'first': 'fear',
                       'second': 'surprise',
                       'third':'ruthless efficiency',
                       'forth':'fanatical devotion',
                       'fifth': None}
    dict_comprehension = {k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}

    print('first' in dict_comprehension)
    print('FIRST' in dict_comprehension)
    print('len of dict_of_weapons:', len(dict_of_weapons))
    print('len of dict_comprehension:', len(dict_comprehension))

# dict_comp()

# COUNT EVEN NUMBERS #
def count_evens(nums):
    comp = [myNum for myNum in nums if myNum % 2 == 0]
    return len(comp)

# print('>>>Count even numbers <<<')
# print(count_evens([2, 1, 2, 3, 4]))
# print(count_evens([2, 2, 0]))
# print(count_evens([1, 3, 5]))
# print()

print('>>> Dict and Set Comprehension <<<')

def dict_comp():
    
    food_prefs = {"name": "Chris", "city": "Seattle", "cake": "chocolate",
                    "fruit": "mango", "salad": "greek", "pasta": "lasagna"}

    #1.
    dict_answer = ['{} is from {}, and he likes {} cake, {} fruit, {} salad, and {} pasta.'.format(food_prefs['name'],food_prefs['city'],food_prefs['cake'],food_prefs['fruit'],food_prefs['salad'],food_prefs['pasta'])]
    # print(dict_answer)

    #2.
    for i in range(16):
        print(hex(i))

    num_hex_list = [(myNum, myHex) for myNum in range(16) for myHex in hex(myNum)]
    print(num_hex_list)

dict_comp()

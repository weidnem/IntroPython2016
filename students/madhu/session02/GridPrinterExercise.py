def print_grid(n):

    plus = '+'
    minus = '- '
    total_minus_spaces = n - 2
    
    for i in range(0,n-1):
        print (plus + ' ' + (minus*size)  + plus + ' ' + (minus*size) + plus)
        for i in range(0,size):
            print ("|" + (spaces * ' ') + "|" + (spaces * ' ') + "|" + (spaces * ' '))
    


print_grid(5)

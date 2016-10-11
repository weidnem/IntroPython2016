def fibonacci(n): #function to print out the nth element in the fibonacci series#
    lst = []
    lst.insert(0,0)
    lst.insert(1,1)
    for i in range(2,n+1):
        value = lst[i-1] + lst[i-2]
        lst.insert(i,value)
    
    print lst[n]


def lucas(n): #function to print out the nth element in the lucas numbers series#
    lst = []
    lst.insert(0,2)
    lst.insert(1,1)
    for i in range(2,n+1):
        value = lst[i-1] + lst[i-2]
        lst.insert(i,value)

    print lst[n]




if __name__ == "__main__":
    fibonacci(10) #calling the fibonacci function to return the 10th element in the series#
    lucas(10) #calling the lucas function to retrun the 10th element in the series#


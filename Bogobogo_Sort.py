import random
from random import *
from time import *

def isSorted(list):
    prev = None
    for x in list:
        if prev != None and (prev > x):
            return False
        prev = x
    return True

def Bogosort(list):
    while (not isSorted(list)):
        shuffle(list)
    return list

def Bogobogosort(list):
    index = 2
    count = 0
    while(not isSorted(list)):
        print(x)
        count += 1
        print(count)
        Bogosort(list[:index])
        index += 1
        if(not isSorted(list[:index])):
            shuffle(list)
            index = 2
    return list

x = []
for i in range(0, 10):
    x.append(randint(0, 100))

start = time()
print ("Before: ", x)
x = Bogobogosort(x)
print ("After: ", x)
print ("%.2f seconds" % (time() - start))

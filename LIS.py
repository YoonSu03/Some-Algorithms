#LIS with Dinamic Programming version.

import time
start_time = time.time()

_arr = [3, 5, 7, 9, 2, 1, 4, 8, 3, 5, 7, 20, 2, 4, 13, 9, 10, 11]
_len = [1]

for i in range(1, len(_arr)):
    _max = 0
    for j in range(len(_len)):
        if _max < _len[j] and _arr[j] < _arr[i]:
            _max = _len[j]
    _len.append(_max + 1)

print(max(_len))

print("--- %s seconds ---" %(time.time() - start_time))

#LIS with None-Dinamic Programing version(from geeksforgeeks.org)

global maximum

def _lis(arr, n):

    global maximum
    if n == 1:
        return 1

    maxEndingHere = 1
    for i in range(1, n):
        res = _lis(arr, i)
        if arr[i - 1] < arr[n - 1] and res + 1 > maxEndingHere:
            maxEndingHere = res + 1
    maximum = max(maximum, maxEndingHere)
    return maxEndingHere


def lis(arr):
    global maximum
    n = len(arr)
    maximum = 1
    _lis(arr, n)
    return maximum

start_time = time.time()

arr = [3, 5, 7, 9, 2, 1, 4, 8, 3, 5, 7, 20, 2, 4, 13, 9, 10, 11]
n = len(arr)
print (lis(arr))

print("--- %s seconds ---" %(time.time() - start_time))

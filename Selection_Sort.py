def selectionsort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for k in range(i+1, len(arr)):
            if arr[k] < arr[min_index]:
                min_index = k
        tmp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = tmp
    return arr

start = time()
print ("Before: ", x)
x = selectionsort(x)
print ("After: ", x)
print ("%.2f seconds" % (time() - start))

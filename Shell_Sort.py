def shellSort(x):
    def gapInsertionSort(x, start, gap):
        for target in range(start + gap, len(x), gap):
            val = x[target]
            i = target
            while i > start:
                if x[i - gap] > val:
                    x[i] = x[i - gap]
                else:
                    break
                i -= gap
            x[i] = val
    gap = len(x) // 2
    while gap > 0:
        for start in range(gap):
            gapInsertionSort(x, start, gap)
        gap = gap // 2
    return x

print([3, 45, 776, 2, 111232, 3321, 332, 223, 1])
print(shellSort([3, 45, 776, 2, 111232, 3321, 332, 223, 1]))
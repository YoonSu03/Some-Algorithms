def radixsort(ordered_list):
    is_sorted = False
    p = 1

    while not is_sorted:
        is_sorted = True
        queue = [list() for _ in range(10)]

        for num in ordered_list:
            digit = (int)(num / p) % 10
            queue[digit].append(num)
            if is_sorted and digit > 0:
                is_sorted  = False

        index = 0
        for numbers in queue:
            for num in numbers:
                ordered_list[index] = num
                index += 1

        p *= 10
    return ordered_list

print([3, 45, 776, 2, 111232, 3321, 332, 223, 1])
print(radixsort([3, 45, 776, 2, 111232, 3321, 332, 223, 1]))
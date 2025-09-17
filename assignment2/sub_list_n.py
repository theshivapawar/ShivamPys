def sub_lists(numbers, n):
    large_list = []
    small_list = []

    for i in range(len(numbers)):
        if (i + 1) % n == 0:
            small_list.append(numbers[i])
            large_list.append(small_list)
            small_list = []
        else:
            small_list.append(numbers[i])
    large_list.append(small_list)

    return large_list


print(sub_lists([1, 2, 3, 4, 5, 6, 7], 2))
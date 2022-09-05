import random


def partition(arr, i, j):
    pivot = arr[random.randint(i, j)]

    less = []
    equal = []
    greater = []

    for elem in arr:
        if elem < pivot:
            less.append(elem)
        elif elem > pivot:
            greater.append(elem)
        else:
            equal.append(elem)

    concat = less + equal + greater
    for x in range(i, j):
        arr[x] = concat[x]

    return len(less)


def quick_sort(arr, i, j):
    if i >= j:
        return

    partition_index = partition(arr, i, j)

    quick_sort(arr, partition_index + 1, j)
    quick_sort(arr, i, partition_index - 1)

    pass


arr = [1, 5, 3, 2, 2, 3, 8, 10, 4, 6]

quick_sort(arr, 0, len(arr) - 1)

print(arr)

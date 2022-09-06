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


def merge(arr1, arr2):
    i = 0
    j = 0

    out = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            out.append(arr1[i])
            i += 1
        else:
            out.append(arr2[j])
            j += 1

    while i < len(arr1):
        out.append(arr1[i])
        i += 1

    while j < len(arr2):
        out.append(arr2[j])
        j += 1

    return out


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2

    sorted_l = merge_sort(arr[:mid])
    sorted_r = merge_sort(arr[mid:])

    return merge(sorted_l, sorted_r)


arr = [1, 5, 3, 2, 2, 3, 8, 10, 4, 6]

# quick_sort(arr, 0, len(arr) - 1)
# print(arr)

print(merge_sort(arr))

def bsearch_r(arr, elem, i, j):
    if i > j:
        return False

    mid = (i + j) // 2

    if arr[mid] == elem:
        return True
    elif elem > arr[mid]:
        return bsearch_r(arr, elem, mid + 1, j)
    else:
        return bsearch_r(arr, elem, i, mid - 1)


def bsearch_i(arr, elem):
    i = 0
    j = len(arr) - 1

    while True:
        if i > j:
            return False

        mid = (i + j) // 2

        if arr[mid] == elem:
            return True
        elif elem > arr[mid]:
            i = mid + 1
        else:
            j = mid - 1


arr = [1, 2, 2, 2, 3, 4, 6, 7, 10, 15, 15, 18]
elem = 19

print(bsearch_r(arr, elem, 0, len(arr) - 1))
print(bsearch_i(arr, elem))

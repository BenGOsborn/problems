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


def mergesort(arr):
    if len(arr) < 2:
        return arr

    middle = len(arr) // 2

    s_left = mergesort(arr[:middle])
    s_right = mergesort(arr[middle:])

    return merge(s_left, s_right)


print(mergesort([1, 5, 4, 2, 8, 3, 2]))

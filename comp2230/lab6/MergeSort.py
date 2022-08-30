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


def mergesort_r(arr):
    if len(arr) < 2:
        return arr

    middle = len(arr) // 2

    s_left = mergesort_r(arr[:middle])
    s_right = mergesort_r(arr[middle:])

    return merge(s_left, s_right)


def mergesort_i(arr):
    split_q = [[elem] for elem in arr]

    while len(split_q):
        elem_1 = split_q.pop(0)

        if len(elem_1) == len(arr):
            return elem_1

        elem_2 = split_q.pop(0)

        split_q.append(merge(elem_1, elem_2))


print(mergesort_i([1, 5, 4, 2, 8, 3, 2]))

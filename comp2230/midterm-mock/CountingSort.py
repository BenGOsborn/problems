def counting_sort(arr, k):
    size = len(arr)
    count = [0] * k

    for i in range(size):
        count[arr[i]] += 1

    for i in range(1, k):
        count[i] += count[i - 1]

    out = [0] * size

    i = size - 1
    while i >= 0:
        out[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    return out


arr = [4, 2, 2, 8, 3, 3, 1, 10]
k = 11

print(counting_sort(arr, k))

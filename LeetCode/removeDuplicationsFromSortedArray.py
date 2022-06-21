tests = [[1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]


def remove_duplicates_from_sorted(arr):
    seen = {}
    out = []

    for i in arr:
        if i not in seen:
            seen[i] = True
            out.append(i)
    
    for i in range(len(out)):
        arr[i] = out[i]

    return len(out)

test = tests[0]

out = remove_duplicates_from_sorted(test)
print(out, test)
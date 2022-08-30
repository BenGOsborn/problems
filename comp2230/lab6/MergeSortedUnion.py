# Algorithm
# ** Both arrays are sorted in ascending order **
# - We will run a standard merge algorithm, but we will also track elements we have already seen in a hashmap (we probably don't even need a hashmap - just need to check that the last value is the same)
# - We will check both arrays and look for the smallest value from each
# - If the value is already part of the uniom, pop it off and void it
# - Otherwise, add the element to the end of the union array and then add it to the seen list

def merge_sorted_union(arr1, arr2):
    i = 0
    j = 0

    out = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if len(out) != 0:
                last = out[-1]

                if arr1[i] != last:
                    out.append(arr1[i])

            else:
                out.append(arr1[i])

            i += 1
        else:
            if len(out) != 0:
                last = out[-1]

                if arr2[j] != last:
                    out.append(arr2[j])

            else:
                out.append(arr2[j])

            j += 1

    while i < len(arr1):
        if len(out) != 0:
            last = out[-1]

            if arr1[i] != last:
                out.append(arr1[i])

        else:
            out.append(arr1[i])

        i += 1

    while j < len(arr2):
        if len(out) != 0:
            last = out[-1]

            if arr2[j] != last:
                out.append(arr2[j])

        else:
            out.append(arr2[j])

        j += 1

    return out


arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4, 5, 6]

print(merge_sorted_union(arr1, arr2))

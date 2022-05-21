def mergeArrays(a, b):
    a_index = 0
    b_index = 0
    result = []

    # Iterate through and find the next greatest from the sorted list
    while a_index < len(a) and b_index < len(b):
        if a[a_index] < b[b_index]:
            result.append(a[a_index])
            a_index += 1
        else:
            result.append(b[b_index])
            b_index += 1

    # At the end just concatenate the remainder of both to ensure all values in the sorted array
    result += a[a_index:]
    result += b[b_index:]

    return result

def main():
    arr1 = [1, 2, 3]
    arr2 = [2, 5, 5]

    print(mergeArrays(arr1, arr2))

if __name__ == "__main__":
    main();
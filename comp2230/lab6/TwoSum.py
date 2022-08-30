# Runs in O(n) time complexity with O(n) space complexity

def two_sum(arr, val):
    mapping = {}
    for val in arr:
        if val not in mapping:
            mapping[val] = 1
        else:
            mapping[val] += 1

    for elem in arr:
        diff = val - elem

        if diff in elem:
            if diff == elem:
                if mapping[diff] > 1:
                    return True
            else:
                return True

    return False

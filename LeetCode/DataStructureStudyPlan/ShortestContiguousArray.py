tests = [[1,2,2,3,1], [1,2,2,3,1,4,2]]

# Easiest solution
def shortest_contiguous(nums):
    seen = {}  

    for elem in nums:
        if elem in seen:
            seen[elem] += 1
        else:
            seen[elem] = 1

    degree = max(seen.values())
    included = []

    for key in seen.keys():
        if seen[key] == degree:
            included.append(key)
    
    out = {}
    for i in included:
        out[i] = 0

        for j in nums:
            if j == i:
                break

            out[i] += 1

        for j in nums[::-1]:
            if j == i:
                break

            out[i] += 1
    
    return len(nums) - max(out.values())

test = tests[1]
print(shortest_contiguous(test))
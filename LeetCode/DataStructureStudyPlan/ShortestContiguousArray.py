tests = [[1,2,2,3,1], [1,2,2,3,1,4,2]]

# Easiest solution
def shortest_contiguous(nums):
    seen = {}  

    for elem in nums:
        if elem in seen:
            seen[elem] += 1
        else:
            seen[elem] = 1

    # **** There could be multiple of the same degree that we have to find

    degree = max(seen.values())
    included = []

    for key in seen.keys():
        if seen[key] == degree:
            included.append(key)
    
    print(included)

test = tests[0]
print(shortest_contiguous(test))
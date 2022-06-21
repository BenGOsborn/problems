tests = [[1,2,3,1], [1,1,1,3,3,4,3,2,4,2]]

def contains_duplicate(nums):
    seen = {}

    for elem in nums:
        if elem in seen:
            return True
        else:
            seen[elem] = True 
    
    return False

test = tests[0]
print(contains_duplicate(test))
tests = [[-2,1,-3,4,-1,2,1,-5,4], [1], [5,4,-1,7,8]]

# Using Kadane's algorithm
def max_subarray(nums):
    cum_sum = max(nums)
    current_sum = 0

    for elem in nums:
        current_sum += elem

        if current_sum < 0:
            current_sum = 0
        else:
            cum_sum = max(cum_sum, current_sum)
    
    return cum_sum

test = tests[0]
print(max_subarray(test))
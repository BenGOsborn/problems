class Solution:
    def sortColors(self, nums):
        x = [0, 0, 0]
        
        for elem in nums:
            x[elem] += 1
    
        i = 0
        for index, elem in enumerate(x):
            curr_i = i
            for j in range(curr_i, curr_i + elem):
                nums[j] = index
                i += 1

tests = [[2,0,2,1,1,0], [2, 0, 1]]

for test in tests:
    Solution().sortColors(test)
    print(test)
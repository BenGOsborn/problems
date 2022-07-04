class Solution:
    def majorityElement(self, nums):
        candidate = nums[0]
        count = 0

        for elem in nums:
            if elem == candidate:
                count += 1
            elif count == 0:
                candidate = elem
                count = 1
            else:
                count -= 1
        
        return candidate
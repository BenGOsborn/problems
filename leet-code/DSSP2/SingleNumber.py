class Solution:
    def singleNumber(self, nums):
        out = 0
        for elem in nums:
            out = out ^ elem
        return out
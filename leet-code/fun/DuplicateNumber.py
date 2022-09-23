class Solution:
    def findDuplicate(self, nums):
        # We don't have to worry about nums[i] == i because it means we will never be able to get to this node unless we start on it, which we won't as 0 is not included and we start on 0

        # **** There is some problem with this but I do not know where - fix it later (https://leetcode.com/problems/find-the-duplicate-number/submissions/)

        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # **** We have to actually loop through this until we find the node at the end - https://youtu.be/wjYnzkAhcNk


tests = [
    [1, 3, 4, 2, 2],
    [3, 1, 3, 4, 2],
    [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
]

for test in tests:
    print(Solution().findDuplicate(test))

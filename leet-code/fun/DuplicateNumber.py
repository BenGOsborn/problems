class Solution:
    def findDuplicate(self, nums):
        # We don't have to worry about nums[i] == i because it means we will never be able to get to this node unless we start on it, which we won't as 0 is not included and we start on 0

        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            for _ in range(2):
                fast = nums[fast]

            if slow == fast:
                return slow


tests = [[1, 3, 4, 2, 2], [3, 1, 3, 4, 2]]

for test in tests:
    print(Solution().findDuplicate(test))

class Solution:
    def findDuplicate(self, nums):
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow


tests = [
    [1, 3, 4, 2, 2],
    [3, 1, 3, 4, 2],
    [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
]

for test in tests:
    print(Solution().findDuplicate(test))

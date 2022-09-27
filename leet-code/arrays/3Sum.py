class Solution:
    def threeSum(self, nums):
        pass


tests = [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 1, 1], []),
    ([0, 0, 0], [[0, 0, 0]])
]

for test in tests:
    print(Solution().threeSum(*test[0]))
    print(test[1])
    print()

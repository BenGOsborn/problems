class Solution:
    def lengthOfLIS(self, nums):
        pass


tests = [
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([0, 1, 0, 3, 2, 3], 4),
    ([7, 7, 7, 7, 7, 7, 7], 1)
]

for test in tests:
    print(Solution().lengthOfLIS(test[0]), test[1])

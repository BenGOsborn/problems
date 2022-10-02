# Algorithm
# - Use a bottom up solution to build from the right to the left
# - Keep track of the maximum increasing subsequence
# - For each subsequence that we look at, look at if it is greater than the previous value, and if it is update it to the max

class Solution:
    def lengthOfLIS(self, nums):
        cache = [1] * len(nums)

        mx = 1

        for i in range(len(nums) - 1, -1, -1):
            local_max = 1

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    local_max = max(local_max, 1 + cache[j])

            cache[i] = local_max
            mx = max(mx, local_max)

        return mx


tests = [
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([0, 1, 0, 3, 2, 3], 4),
    ([7, 7, 7, 7, 7, 7, 7], 1)
]

for test in tests:
    print(Solution().lengthOfLIS(test[0]), test[1])

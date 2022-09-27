class Solution:
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        max_container = 0

        while i < j:
            max_container = max(max_container, (j - i) *
                                min(height[i], height[j]))

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_container


tests = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1)
]


for test in tests:
    print(Solution().maxArea(test[0]))
    print(test[1])
    print()

class Solution:
    def maxArea(self, height):
        pass


tests = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1)
]


for test in tests:
    print(Solution().maxArea(test[0]))
    print(test[1])
    print()

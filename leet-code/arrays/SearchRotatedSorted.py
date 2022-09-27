class Solution:
    def search(self, nums, target):
        pass


tests = [
    (([4, 5, 6, 7, 0, 1, 2], 0), 4),
    (([4, 5, 6, 7, 0, 1, 2], 3), -1),
    (([1], 0), -1)
]

for test in tests:
    print(Solution().search(*test[0]))
    print(test[1])
    print()

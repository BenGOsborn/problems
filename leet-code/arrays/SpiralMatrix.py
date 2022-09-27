class Solution:
    def spiralOrder(self, matrix):
        pass


tests = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5])
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
     [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
]

for test in tests:
    print(Solution().spiralOrder(test[0]))
    print(test[1])
    print()

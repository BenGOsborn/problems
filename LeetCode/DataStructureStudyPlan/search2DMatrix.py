tests = [
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
]

# **** The way that we are going to solve this one is to treat it like a regular binary
# search where we first get the total number of elements, start at the center, but all we need is to just modulo our new position by the rows and cols


class Solution:
    def searchMatrix(self, matrix, target):
        pass


test = tests[0]
print(Solution().searchMatrix(test[0], test[1]))

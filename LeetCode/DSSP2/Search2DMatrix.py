class Solution:
    def binary_search_col(self, matrix, col, top, bot, target):
        mid = (top + bot) // 2

        if matrix[mid][col] == target:
            return True
        else:
            if top >= bot:
                return False
            elif matrix[mid][col] > target:
                return self.binary_search_col(matrix, col, top, mid - 1, target)
            else:
                return self.binary_search_col(matrix, col, mid + 1, bot, target)

    def binary_search_helper(self, matrix, start, end, target):
        row_index = len(matrix) - 1

        mid = (start + end) // 2

        if self.binary_search_col(matrix, mid, 0, row_index, target):
            return True
        else:
            if start >= end:
                return False
            elif matrix[0][mid] > target:
                return self.binary_search_helper(matrix, start, mid - 1, target)
            else:
                return self.binary_search_helper(matrix, mid + 1, end, target)


    def searchMatrix(self, matrix, target):
        return self.binary_search_helper(matrix, 0, len(matrix[0]) - 1, target)

tests = [
    ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5),
    ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20),
    ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 7)
    ]

for test in tests:
    print(Solution().searchMatrix(test[0], test[1]))
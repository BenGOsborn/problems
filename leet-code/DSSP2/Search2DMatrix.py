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

    def searchMatrix(self, matrix, target):
        row_index = len(matrix) - 1

        for i in range(len(matrix[0])):
            if self.binary_search_col(matrix, i, 0, row_index, target):
                return True
        
        return False

tests = [
    ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5),
    ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20),
    ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 11),
    ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 13),
    ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 7)
    ]

for test in tests:
    print(Solution().searchMatrix(test[0], test[1]))
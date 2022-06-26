tests = [
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
]


class Solution:
    def search(self, matrix, start_row, start_col, end_row, end_col, target):
        cols = len(matrix[0])

        middle = (start_row * cols + start_col + end_row * cols + end_col) // 2
        middle_index_row = middle // cols
        middle_index_col = middle % cols

        middle_value = matrix[middle_index_row][middle_index_col]

        if middle_value == target:
            return True
        elif start_row >= end_row and start_col >= end_col:
            return False
        elif middle_value < target:
            return self.search(matrix, start_row, start_col, middle_index_row, middle_index_col, target)
        else:
            return self.search(matrix, middle_index_row, middle_index_col, end_row, end_col, target)

    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])

        return self.search(matrix, 0, 0, rows - 1, cols - 1, target);


test = tests[0]
print(Solution().searchMatrix(test[0], test[1]))

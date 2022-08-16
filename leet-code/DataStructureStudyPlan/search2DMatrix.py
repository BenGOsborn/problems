tests = [
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 16),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
]


class Solution:
    def increment_index(self, cols, row, col):
        if col == cols - 1:
            return (row + 1, 0)
        return (row, col + 1)

    def decrement_index(self, cols, row, col):
        if col == 0:
            return (row - 1, cols - 1)
        return (row, col - 1)
    
    def search(self, matrix, start_row, start_col, end_row, end_col, target):
        cols = len(matrix[0])

        start_size = start_row * cols + start_col
        end_size = end_row * cols + end_col

        if start_size > end_size:
            return False
        
        middle = (start_size + end_size) // 2
        middle_index_row = middle // cols
        middle_index_col = middle % cols

        middle_value = matrix[middle_index_row][middle_index_col]

        if middle_value == target:
            return True
        elif middle_value < target:
            incremented_middle = self.increment_index(cols, middle_index_row, middle_index_col)
            return self.search(matrix, incremented_middle[0], incremented_middle[1], end_row, end_col, target)
        else:
            decremented_middle = self.decrement_index(cols, middle_index_row, middle_index_col)
            return self.search(matrix, start_row, start_col, decremented_middle[0], decremented_middle[1], target)

    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])

        return self.search(matrix, 0, 0, rows - 1, cols - 1, target);


test = tests[1]
print(Solution().searchMatrix(test[0], test[1]))

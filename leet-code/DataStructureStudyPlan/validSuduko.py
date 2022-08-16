
tests = [
    [["5", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
    [["8", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
]

class Solution:
    def check_row(self, matrix, row):
        seen = {}

        for elem in matrix[row]:
            if elem in seen and elem != ".":
                return False

            seen[elem] = True
        
        return True

    def check_col(self, matrix, col):
        seen = {}

        for row in range(len(matrix)):
            elem = matrix[row][col]

            if elem in seen and elem != ".":
                return False

            seen[matrix[row][col]] = True
        
        return True

    def check_square(self, matrix, row, col, size):
        seen = {}        

        for i in range(size):
            for j in range(size):
                elem = matrix[row + i][col + j]

                if elem in seen and elem != ".":
                    return False

                seen[elem] = True

        return True

    def isValidSudoku(self, board):
        for i in range(len(board)):
            if not self.check_row(board, i):
                return False
        
        for i in range(len(board[0])):
            if not self.check_col(board, i):
                return False
        
        size = 3
        for i in range(len(board) // size):
            for j in range(len(board[0]) // size):
                if not self.check_square(board, i * size, j * size, size):
                    return False
        
        return True



test = tests[1]
print(Solution().isValidSudoku(test))

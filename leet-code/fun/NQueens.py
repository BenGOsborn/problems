class Solution:
    def is_valid_pos(self, board, row, col):
        for i in range(row):
            if board[i][col] == 1:
                return False

        for i in range(col):
            if board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1),
                        range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row, len(board[0])),
                        range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row, -1, -1),
                        range(col, len(board))):
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row, len(board[0])),
                        range(col, len(board))):
            if board[i][j] == 1:
                return False

        return True

    def copy_board(self, board):
        return [row[:] for row in board]

    def find_queens(self, board, current_row, out):
        if current_row == len(board):
            copy = self.copy_board(board)
            out.append(copy)

        for i in range(len(board[0])):
            if self.is_valid_pos(board, current_row, i):
                board[current_row][i] = 1

                self.find_queens(board, current_row + 1, out)

                board[current_row][i] = 0

    def solveNQueens(self, n):
        board = [[0 for _ in range(n)] for _ in range(n)]

        out = []

        self.find_queens(board, 0, out)

        for i in range(len(out)):
            for j in range(len(out[i])):
                temp = "".join("." if x == 0 else "Q" for x in out[i][j])
                out[i][j] = temp

        return out


solution = Solution()

print(solution.solveNQueens(4))

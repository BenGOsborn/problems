# Algorithm
# - We are going to recursively call the find queens on the next row, and keep track of the current column with the for loop
# - If we cant find a given row for the current one, we need to return false or true to let the previous know
# - If we return true, then we can copy this back up the callstack to break out of the function
# Assume that we are given an NxN board


# With assistance from https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/
def is_valid_pos(board, row, col):
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

    return True


def find_queens(board, current_row):
    if current_row == len(board):
        return True

    for i in range(len(board[0])):
        is_valid = is_valid_pos(board, current_row, i)

        if is_valid:
            board[current_row][i] = 1

            found = find_queens(board, current_row + 1)

            if found:
                return True

            board[current_row][i] = 0

    return False


def print_board(board):
    for row in board:
        print(row)


size = 4
board = [[0 for _ in range(4)] for _ in range(4)]
print_board(board)
print()
find_queens(board, 0)
print_board(board)

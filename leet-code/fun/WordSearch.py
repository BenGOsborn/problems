class Solution:
    def dfs(self, board, word, i, j, n):
        if not (i >= 0 and i < len(board) and j >= 0 and j < len(board[0])):
            return False

        if board[i][j] == "#":
            return False

        if board[i][j] != word[n]:
            return False
        if n == len(word) - 1:
            return True

        temp = board[i][j]
        board[i][j] = "#"

        for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if self.dfs(board, word, i + y, j + x, n + 1):
                return True

        board[i][j] = temp

        return False

    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.dfs(board, word, i, j, 0):
                    return True

        return False


tests = [
    # ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"),
    # ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"),
    # ([["a"]], "a"),
    # ([["a", "b"], ["c", "d"]], "cdba"),
    # ([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS"),
    ([["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], [
     "A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "B"], ["A", "A", "A", "A", "B", "A"]], "AAAAAAAAAAAAABB")
]

for test in tests:
    print(Solution().exist(*test))

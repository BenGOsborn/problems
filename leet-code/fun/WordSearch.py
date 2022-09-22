class Solution:
    def dfs(self, board, word, i, j, n):
        if n == len(word) - 1:
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == "#" or board[i][j] != word[n]:
            return False

        temp = board[i][j]
        board[i][j] = "#"

        res = self.dfs(board, word, i + 1, j, n + 1) or \
            self.dfs(board, word, i - 1, j, n + 1) or \
            self.dfs(board, word, i, j + 1, n + 1) or \
            self.dfs(board, word, i, j - 1, n + 1)

        board[i][j] = temp

        return res

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

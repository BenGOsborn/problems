class Solution:
    def encode(self, i, j):
        return f"{i},{j}"

    def dfs(self, board, word, i, j, n, seen):
        # **** Now I need to reimplement the cycle detection system for a particular path
        # **** There should be a better way of doing this with only one batch of memory...

        encoded = self.encode(i, j)
        if encoded in seen:
            return False

        if board[i][j] != word[n]:
            return False
        if n == len(word) - 1:
            return True

        seen[encoded] = True

        if i > 0 and i < len(board) and self.dfs(board, word, i - 1, j, n + 1, seen.copy()):
            return True
        if i >= 0 and i < len(board) - 1 and self.dfs(board, word, i + 1, j, n + 1, seen.copy()):
            return True
        if j > 0 and j < len(board[0]) and self.dfs(board, word, i, j - 1, n + 1, seen.copy()):
            return True
        if j >= 0 and j < len(board[0]) - 1 and self.dfs(board, word, i, j + 1, n + 1, seen.copy()):
            return True

        return False

    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.dfs(board, word, i, j, 0, {}):
                    return True

        return False


tests = [
    ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"),
    ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"),
    ([["a"]], "a"),
    ([["a", "b"], ["c", "d"]], "cdba"),
    ([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS")
]

for test in tests:
    print(Solution().exist(*test))

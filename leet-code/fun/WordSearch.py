class Solution:
    def dfs():
        pass

    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[i])):
                pass


tests = [
    ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"),
    ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB")
]

for test in tests:
    print(Solution().exist(*test))

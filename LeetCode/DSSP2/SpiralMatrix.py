from calendar import c


class Solution:
    def generateMatrix(self, n):
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        left_col = 0
        right_col = n - 1
        top_row = 0
        bot_row = n - 1

        j = [0, 0]

        # **** The process is that we will travel around in different directions, then when we hit our end state we will move it into a new state (like a FSM)

        for i in range(1, n ** 2 + 1):
            matrix[j[0]][j[1]] = i

            if j[0] == top_row and j[1] == right_col:
                j[0] += 1
            elif j[0] == bot_row and j[1] == right_col:
                j[1] -= 1
            elif j[0] == bot_row and j[1] == left_col:
                j[0] -= 1
            elif j[0] == top_row + 1 and j[1] == left_col:
                j[1] += 1
                left_col += 1
                right_col -= 1
                bot_row += 1
                top_row -= 1
            elif j[0] == top_row:
                j[1] += 1
            elif j[1] == right_col:
                j[0] += 1
            elif j[0] == bot_row:
                j[1] -= 1
            elif j[1] == left_col:
                j[0] -= 1

        return matrix

out = Solution().generateMatrix(4)
for row in out:
    print(row)
# Algorithm
# - Record the max of the i and j directions that we can currently go towards
# - For each position, move accordingly based on where we are in the min or the max

class Solution:
    def spiralOrder(self, matrix):
        min_i = 0
        max_i = len(matrix) - 1
        min_j = 0
        max_j = len(matrix[0]) - 1

        out = []

        i = 0
        j = 0

        # When we get to the node that is just before the min node, we will update the mins and the max and then we will play accordingly to that

        while max_i >= min_i and max_j >= min_j:
            out.append(matrix[i][j])

            if i == min_i - 1 and j == min_j:
                min_j += 1
                j += 1
            elif i == max_i and j == min_j:
                max_i -= 1
                i -= 1
            elif i == max_i and j == max_j:
                max_j -= 1
                j -= 1
            elif i == min_i and j == max_j:
                min_i += 1
                i += 1
            elif i == min_i:
                j += 1
            elif j == max_j:
                i += 1
            elif i == max_j:
                j -= 1
            elif j == min_j:
                i -= 1

        return out


tests = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    # ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
    #  [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
]

for test in tests:
    print(Solution().spiralOrder(test[0]))
    print(test[1])
    print()

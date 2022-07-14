class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Transpose
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse horizontally
        for i in range(len(matrix)):
            l = 0
            r = len(matrix[0]) - 1

            while r > l:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1
                r -= 1

test = [[1,2,3],[4,5,6],[7,8,9]]

Solution().rotate(test)
print(test)
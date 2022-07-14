class Solution:
    def binary_search_col(self, matrix, c, t, b, target):
        mid = (t + b) // 2

        if matrix[mid][c] == target:
            return True
        else:
            if t >= b:
                return False
            elif matrix[mid][c] > target:
                return self.binary_search_col(matrix, c, t, mid - 1, target)
            else:
                return self.binary_search_col(matrix, c, mid + 1, b, target)

    def searchMatrix(self, matrix, target):
        print(matrix, target)
        print(self.binary_search_col(matrix, 2, 0, 4, 13))

        # **** The way we will do this is by doing a binary search for each column we select,
        # but we will select columns based off of their range between the minimum of the furthest left column and the max of the furthest right column (using our selected column as the median)
        # **** This way, we are effectively doing a binary search for our binary searches resulting in (logn) ** 2 time

        pass


tests = [([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5), ([
    [1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20)]

for test in tests:
    print(Solution().searchMatrix(test[0], test[1]))
class Solution:
    def binary_search_col(self, matrix, col, top, bot, target):
        mid = (top + bot) // 2

        if matrix[mid][col] == target:
            return True
        else:
            if top >= bot:
                return False
            elif matrix[mid][col] > target:
                return self.binary_search_col(matrix, col, top, mid - 1, target)
            else:
                return self.binary_search_col(matrix, col, mid + 1, bot, target)

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
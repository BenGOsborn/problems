class Solution:
    def searchMatrix(self, matrix, target):
        # **** The way we will do this is by doing a binary search for each column we select,
        # but we will select columns based off of their range between the minimum of the furthest left column and the max of the furthest right column (using our selected column as the median)
        # **** This way, we are effectively doing a binary search for our binary searches resulting in (logn) ** 2 time

        pass 
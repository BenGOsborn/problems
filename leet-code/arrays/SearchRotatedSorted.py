# Algorithm
# - Run a binary search, but we are going to do segmentation based comparisons
# - If there exists an element on the right such that it is less than, if our mid is less than that amount, we will search in there, otherwise, we will search the other section
# - In the event that we do not have such a case, we will just do a regular binary search

class Solution:
    def bin_search(self, nums, target, i, j):
        if i > j:
            return -1

        mid = (i + j) // 2
        print(i, j, mid, nums[i], nums[j], nums[mid], target)

        if nums[mid] == target:
            return mid

        if target > nums[mid]:
            return self.bin_search(nums, target, mid + 1, j)

        # **** This gets interrupted by the previous one first - we need to consider these cases individually
        if target >= nums[i]:
            return self.bin_search(nums, target, i, mid - 1)

        return self.bin_search(nums, target, mid + 1, j)

    def search(self, nums, target):
        return self.bin_search(nums, target, 0, len(nums) - 1)


tests = [
    # (([4, 5, 6, 7, 0, 1, 2], 0), 4),
    # (([4, 5, 6, 7, 0, 1, 2], 3), -1),
    # (([1], 0), -1),
    (([4, 5, 6, 7, 8, 1, 2, 3], 8), 4)
]

for test in tests:
    print(Solution().search(*test[0]))
    print(test[1])
    print()

# Algorithm
# - Run a binary search, but we are going to do segmentation based comparisons
# - If there exists an element on the right such that it is less than, if our mid is less than that amount, we will search in there, otherwise, we will search the other section
# - In the event that we do not have such a case, we will just do a regular binary search

class Solution:
    def bin_search(self, nums, target, i, j):
        if i > j:
            return -1

        mid = (i + j) // 2

        if target == nums[mid]:
            return mid

        if nums[mid] >= nums[i] and nums[j] >= nums[mid]:  # i < mid, mid < j
            if target > nums[mid]:
                return self.bin_search(nums, target, mid + 1, j)
            return self.bin_search(nums, target, i, mid - 1)
        elif nums[mid] > nums[i] and nums[mid] > nums[j]:  # i < mid, mid > j
            if target > nums[mid]:
                return self.bin_search(nums, target, mid + 1, j)

            if target >= nums[i]:
                return self.bin_search(nums, target, i, mid - 1)

            return self.bin_search(nums, target, mid + 1, j)
        elif nums[mid] < nums[i] and nums[j] > nums[mid]:  # i > mid, mid < j
            if target < nums[mid]:
                return self.bin_search(nums, target, i, mid - 1)

            if target <= nums[j]:
                return self.bin_search(nums, target, mid + 1, j)

            return self.bin_search(nums, target, i, mid - 1)

    def search(self, nums, target):
        return self.bin_search(nums, target, 0, len(nums) - 1)


tests = [
    (([4, 5, 6, 7, 0, 1, 2], 0), 4),
    (([4, 5, 6, 7, 0, 1, 2], 3), -1),
    (([1], 0), -1),
    (([4, 5, 6, 7, 8, 1, 2, 3], 8), 4),
    (([6, 7, 8, 1, 2, 3, 4, 5], 8), 2),
    (([1, 2, 3], 8), -1)
]

for test in tests:
    print(Solution().search(*test[0]))
    print(test[1])
    print()

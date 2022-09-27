class Solution:
    def bin_search_first(self, nums, target, i, j):
        if i > j:
            return -1

        mid = (i + j) // 2

        if nums[mid] == target and (mid == 0 or nums[mid - 1] < target):
            return mid
        elif target > nums[mid]:
            return self.bin_search_first(nums, target, mid + 1, j)
        else:
            return self.bin_search_first(nums, target, i, mid - 1)

    def bin_search_last(self, nums, target, i, j):
        if i > j:
            return -1

        mid = (i + j) // 2

        if nums[mid] == target and (mid == len(nums) - 1 or nums[mid + 1] > target):
            return mid
        elif target >= nums[mid]:
            return self.bin_search_last(nums, target, mid + 1, j)
        else:
            return self.bin_search_last(nums, target, i, mid - 1)

    def searchRange(self, nums, target):
        first = self.bin_search_first(nums, target, 0, len(nums) - 1)
        if first == -1:
            return [-1, -1]
        return [first, self.bin_search_last(nums, target, 0, len(nums) - 1)]


tests = [
    (([5, 7, 7, 8, 8, 10], 8), [3, 4]),
    (([5, 7, 7, 8, 8, 10], 6), [-1, -1]),
    (([], 0), [-1, -1]),
    (([1, 1, 2], 1), [0, 1])
]

for test in tests:
    print(Solution().searchRange(*test[0]))
    print(str(test[1]) + "\n")

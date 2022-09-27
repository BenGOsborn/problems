class Solution:
    def binary_search(self, nums, target, i, j):
        if i > j:
            return -1

        mid = (i + j) // 2

        if nums[mid] == target and (mid == len(nums) - 1 or nums[mid + 1] != target):
            return mid
        elif target >= nums[mid]:
            return self.binary_search(nums, target, mid + 1, j)
        else:
            return self.binary_search(nums, target, i, mid - 1)

    def twoSum(self, numbers, target):
        for i, elem in enumerate(numbers):
            index = self.binary_search(
                numbers, target - elem, 0, len(numbers) - 1)
            if index != -1 and i != index:
                return [i + 1, index + 1]


tests = [
    (([2, 7, 11, 15], 9), [1, 2]),
    (([2, 3, 4], 6), [1, 3]),
    (([-1, 0], -1), [1, 2]),
    (([1, 2, 3, 4, 4, 9, 56, 90], 8), [4, 5])
]

for test in tests:
    print(Solution().twoSum(*test[0]))
    print(test[1])
    print()

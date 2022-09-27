class Solution:
    def binary_search(self, nums, target, i, j):
        if i > j:
            return -1

        mid = (i + j) // 2

        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            return self.binary_search(nums, target, mid + 1, j)
        else:
            return self.binary_search(nums, target, i, mid - 1)

# **** We need to make sure that the element we search for is not a part of the overall array (which we could get by shifting the rest of the array down one index then mapping it back)

    def twoSum(self, numbers, target):
        for i, elem in enumerate(numbers):
            index = self.binary_search(
                numbers, target - elem, 0, len(numbers) - 1)
            if index != -1:
                return [i + 1, index + 1]


tests = [
    (([2, 7, 11, 15], 9), [1, 2]),
    (([2, 3, 4], 6), [1, 3]),
    (([-1, 0], -1), [1, 2])
]

for test in tests:
    print(Solution().twoSum(*test[0]))
    print(test[1])
    print()

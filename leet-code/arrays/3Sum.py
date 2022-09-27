# Algorithm
# - Sort the array O(nlogn)
# - For all n elements in the array, use this to get the new target value, and then run the two sum for the rest of the array
# - To not get duplicates, maybe we just keep an array of elements that we already have ?

class Solution:
    def threeSum(self, nums):
        target = 0

        nums.sort()


tests = [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 1, 1], []),
    ([0, 0, 0], [[0, 0, 0]])
]

for test in tests:
    print(Solution().threeSum(test[0]))
    print(test[1])
    print()

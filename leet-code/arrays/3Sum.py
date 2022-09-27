# Algorithm
# - Sort the array O(nlogn)
# - For all n elements in the array, use this to get the new target value, and then run the two sum for the rest of the array
# - Once we select our pivot (starting from 0), we will run two sum for the REMAINDER of the array, as previous pivots have already covered all previous solutions using that number
# - Pivots will not use the same number twice, and if we encounter a duplicate number we will skip over it

class Solution:
    def threeSum(self, nums):
        nums.sort()

        pivot = None
        pivot_index = 0

        out = []

        while pivot_index < len(nums):
            if nums[pivot_index] == pivot:
                pivot_index += 1
                continue

            i = pivot_index + 1
            j = len(nums) - 1

            prev_i = None
            prev_j = None

            pivot = nums[pivot_index]
            target = -pivot

            while i < j:
                if nums[i] == prev_i:
                    i += 1
                    continue
                if nums[j] == prev_j:
                    j -= 1
                    continue

                sm = nums[i] + nums[j]

                if sm == target:
                    out.append([pivot, nums[i], nums[j]])
                    prev_i = nums[i]
                    prev_j = nums[j]
                    i += 1
                    j -= 1
                elif sm > target:
                    prev_j = nums[j]
                    j -= 1
                else:
                    prev_i = nums[i]
                    i += 1

            pivot_index += 1

        return out


tests = [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 1, 1], []),
    ([0, 0, 0], [[0, 0, 0]]),
    ([-2, 0, 0, 2, 2], [[-2, 0, 2]])
]

for test in tests:
    print(Solution().threeSum(test[0]))
    print(test[1])
    print()

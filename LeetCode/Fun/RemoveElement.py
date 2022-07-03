tests = [([2, 2, 4, 3], 3)]

class Solution:
    def swap(self, i, j, nums):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def removeElement(self, nums, val):
        k = 0

        start_index = 0
        end_index = len(nums) - 1

        while start_index <= end_index:
            if nums[start_index] == val:
                self.swap(start_index, end_index, nums)
                end_index -= 1
            else:
                start_index += 1
                k += 1

        return k


test = tests[0]
print(Solution().removeElement(test[0], test[1]))
print(test[0])

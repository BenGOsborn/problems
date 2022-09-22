class Solution:
    # def can_jump_h(self, nums, i, cache):
    #     if i in cache:
    #         return cache[i]

    #     if i >= len(nums):
    #         cache[i] = False
    #         return False
    #     if i == len(nums) - 1:
    #         cache[i] = True
    #         return True

    #     for j in range(1, min(nums[i] + 1, len(nums) - i)):
    #         if self.can_jump_h(nums, i + j, cache):
    #             cache[i] = True
    #             return True

    #     cache[i] = False
    #     return False

    # def canJump(self, nums):
    #     return self.can_jump_h(nums, 0, {})

    def canJump(self, nums):
        goal = len(nums) - 1

        for i in list(range(len(nums)))[::-1]:
            if i + nums[i] >= goal:
                goal = i

        return goal == 0


tests = [[2, 3, 1, 1, 4], [3, 2, 1, 0, 4]]

for test in tests:
    print(Solution().canJump(test))

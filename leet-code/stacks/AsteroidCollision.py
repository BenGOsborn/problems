# Algorithm - https://leetcode.com/problems/asteroid-collision/
# - Initialize a stack with all elements initially
# - Pop an element off the stack into a new stack, then compare the top of both stacks for collisions
# - If the popped off element collides and is broken, remove it and move the original stack to the new stack
# - If the popped off element collides and does the breaking, remove the top of the original stack
# - If they are travelling in the same direction, move it to the next stack and repeat the process
# - Repeat this process until the original stack is empty, then we can return this stack as an array
# - Note: positive means right, negative means left (some can never collide)

class Solution:
    def asteroidCollision(self, asteroids):
        main_stack = []
        compare_stack = []

        for asteroid in asteroids:
            main_stack.append(asteroid)
        compare_stack.append(main_stack.pop(-1))

        while len(main_stack):
            if main_stack[-1] > 0 and len(compare_stack) and compare_stack[-1] < 0:
                if abs(main_stack[-1]) > abs(compare_stack[-1]):
                    compare_stack.pop(-1)
                elif abs(main_stack[-1]) < abs(compare_stack[-1]):
                    main_stack.pop(-1)
                    main_stack.append(compare_stack.pop(-1))
                else:
                    main_stack.pop(-1)
                    compare_stack.pop(-1)
            else:
                compare_stack.append(main_stack.pop(-1))

        return compare_stack[::-1]


tests = [
    ([5, 10, -5], [5, 10]),
    ([8, -8], []),
    ([10, 2, -5], [10]),
    ([-2, -1, 1, 2], [-2, -1, 1, 2]),
    ([-2, -2, 1, -1], [-2, -2]),
    ([-2, 2, -1, -2], [-2])
]

for test in tests:
    print(Solution().asteroidCollision(test[0]))
    print(test[1])
    print()

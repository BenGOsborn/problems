class Solution:
    def asteroidCollision(self, asteroids):
        pass


tests = [
    ([5, 10, -5], [5, 10]),
    ([8, -8], []),
    ([10, 2, -5], [10])
]

for test in tests:
    print(Solution().asteroidCollision(test[0]))
    print(test[1])
    print()

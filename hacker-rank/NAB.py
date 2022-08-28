# def solution(A):
#     i = 1

#     while True:
#         if i not in A:
#             return i

#         i += 1

# 1

# def solution(A):
#     ans = A[0]
#     for i in range(1, len(A)):
#         if A[i] < ans:
#             ans = A[i]
#     return ans


# tests = [[2, 1, 4]]

# for test in tests:
#     print(solution(test))

# 2

# Algorithm - adopt a greedy strategy to sum up digits to the correct value, and then print the digits in reverse

# def solution(N):
#     tracker = 0
#     digits = ""

#     while True:
#         if tracker + 9 < N:
#             tracker += 9
#             digits = "9" + digits
#         else:
#             digits = str(N - tracker) + digits

#             return int(digits)


# print(solution(7))

# 3

# Algorithm
# - We will have two pointers from left and right which will move towards each other and terminate when they intersect (and return true if nothing else has been found)
# - At each pointer position, we will check what the other is - 4 cases
#   - Case 1: there are 2 values which are non mysteries - in this case we check if they are equal and if not we break
#   - Case 2: there is 1 value that is a mystery and the other is not - set the value of the mystery to be the other
#   - Case 3: both values are mysteries - choose a for both of them
#   - Case 4: we land in the middle of the array at the end and it is a mystery - choose a random value

def solution(S):
    if S == "":
        return S

    array = [char for char in S]

    left = 0
    right = len(S) - 1

    while left <= right:
        if left == right:
            if array[left] == "?":
                array[left] = "a"
        elif array[left] == "?" and array[right] == "?":
            array[left] = "a"
            array[right] = "a"
        elif array[left] == "?":
            array[left] = array[right]
        elif array[right] == "?":
            array[right] = array[left]
        else:
            if array[left] != array[right]:
                return "NO"

        left += 1
        right -= 1

    return "".join(array)


tests = ["kayak", "radar", "mom", "?ab??a", "bab??a", "?a?", "a", "", "?"]

for test in tests:
    print(solution(test))

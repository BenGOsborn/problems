# Algorithm
# - We will have some output storage array which we will store our results into
# - We will use recursive backtracking to generate all permutations from the remaining characters in the order in which they come
# - We will simply just feed the algorithm a list of numbers (like characters) and run the permutation algorithm as normally
# Time: O(n * n!) | Space: O(n!) (If we want to remove the extra n factor, we could use a linked list)

def permute(current, available, out):
    if len(available) == 0:
        out.append(current)
        return

    for i in range(len(available)):
        permute(current + available[i], available[:i] + available[i + 1:], out)


current = ""
available = [str(x) for x in range(5)]  # This will be N
out = []
permute(current, available, out)
print(out)
print(len(out))

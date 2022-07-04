class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, root, k, seen):
        if not root:
            return False

        if root.val not in seen:
            seen[root.val] = 1
        else:
            seen[root.val] += 1

        if self.helper(root.left, k, seen) or self.helper(root.right, k, seen):
            return True

        look_for = k - root.val

        if look_for in seen:
            if seen[look_for] == root.val:
                return seen[look_for] > 1
            return True

        return False

    def findTarget(self, root, k):
        seen = {}

        return self.helper(root, k, seen)


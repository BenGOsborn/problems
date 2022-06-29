# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root, depth):
        if not root:
            return depth - 1
        
        return max(self.helper(root.left, depth + 1), self.helper(root.right, depth + 1))

    def maxDepth(self, root) -> int:
        return self.helper(root, 1)
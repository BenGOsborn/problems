# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root, out):
        if root == None:
            return

        self.helper(root.left, out)
        out.append(root.val);
        self.helper(root.right, out)

    def inorderTraversal(self, root):
        out = []
        self.helper(root, out)

        return out
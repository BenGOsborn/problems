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
        self.helper(root.right, out)
        out.append(root.val);

    def postorderTraversal(self, root):
        out = []
        self.helper(root, out)

        return out
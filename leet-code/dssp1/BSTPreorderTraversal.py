# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root, out):
        if root == None:
            return

        out.append(root.val);
        self.helper(root.left, out)
        self.helper(root.right, out)

    # Recursive
    def preorderTraversalRecursive(self, root):
        out = []
        self.helper(root, out)

        return out

    # Iterative
    def preorderTraversal(self, root):
        stack = [root]

        out = []

        while stack:
            elem = stack.pop(-1)

            if not elem:
                continue

            out.append(elem.val)
            stack.append(elem.right)
            stack.append(elem.left)

        return out

Solution().preorderTraversal(3)
class Solution:
    def helper(self, root, targetSum, cumSum):
        if not root:
            return False

        if not root.left and not root.right:
            return cumSum + root.val == targetSum

        if self.helper(root.left, targetSum, cumSum + root.val) or self.helper(root.right, targetSum, cumSum + root.val):
            return True
        
        return False

    def hasPathSum(self, root, targetSum):
        return self.helper(root, targetSum, 0)
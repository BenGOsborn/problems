class Solution:
    def helper(self, root, upper_bound, lower_bound):
        if not root:
            return True

        if upper_bound is not None and root.val >= upper_bound:
            return False

        if lower_bound is not None and root.val <= lower_bound:
            return False

        return self.helper(root.left, root.val, lower_bound) and self.helper(root.right, upper_bound, root.val)

    def isValidBST(self, root):
        return self.helper(root, None, None)

# Algorithm
# - Each element needs to be between a lower bound and an upper bound
# - These bounds are established by the direction we traverse the tree - when we traverse left the root value becomes the upper bound, and when we traverse right the root value becomes the lower bound
# - We will have to initialize these bounds initially as optional (or None), as if we keep traversing left / right for example it is unbounded
# - We will do this recursively and update the nodes as we go

# Edge cases
# - When we only have one root we will return valid

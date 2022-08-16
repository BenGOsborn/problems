class Solution:
    def is_mirror(self, left, right):
        if not left and not right:
            return True
        
        if not left or not right:
            return False

        if left.val != right.val:
            return False

        if not self.is_mirror(left.left, right.right) or not self.is_mirror(left.right, right.left):
            return False

        return True

    def isSymmetric(self, root):
        return self.is_mirror(root.left, root.right)
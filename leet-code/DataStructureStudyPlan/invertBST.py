class Solution:
    def invertTree(self, root):
        if not root:
            return
        
        temp = root.right
        root.right = root.left
        root.left = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
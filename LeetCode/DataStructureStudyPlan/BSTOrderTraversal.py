class Solution:
    def post_order_helper(self, root, positions, depth):
        if not root:
            return 

        if depth in positions:
            positions[depth].append(root.val)
        else:
            positions[depth] = [root.val]

        self.post_order_helper(root.left, positions, depth + 1)
        self.post_order_helper(root.right, positions, depth + 1)

    def levelOrder(self, root):
        positions = {}

        self.post_order_helper(root, positions, 1)

        out = []
        for i in range(len(positions.keys())):
            out.append(positions[i + 1])

        return out
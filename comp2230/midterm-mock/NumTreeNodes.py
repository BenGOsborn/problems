class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# Algorithm
# Return 1 + the number of nodes to the left and the right
# If the tree element is null, then we will return 0


def tree_size(root):
    if root is None:
        return 0

    return 1 + tree_size(root.left) + tree_size(root.right)

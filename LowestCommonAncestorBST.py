def insert(root, data):
    if root is None:
        root = Node(data)
    else:
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                insert(root.left, data)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                insert(root.right, data)
    return root


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def contains(root, v):
    if root.data == v:
        return True
    else:
        if v < root.data:
            if root.left is None:
                return False
            else:
                return contains(root.left, v)
        else:
            if root.right is None:
                return False
            else:
                return contains(root.right, v)


def lca(root, v1, v2):
    # **** So basically we are going to start off with the root and then we are going to traversing
    # until we find where the search doesnt contain both, and when we do we are going to return false,
    # and then we will return true on the first one we see

    if contains(root, v1) and contains(v2):
        return 


def main():
    root = None
    root = insert(root, 4)
    root = insert(root, 2)
    root = insert(root, 3)
    root = insert(root, 1)
    root = insert(root, 7)
    root = insert(root, 6)

    print(lca(root, 1, 7))

if __name__ == "__main__":
    main()

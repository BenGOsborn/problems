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


def print_tree(root, spaces):
    if root:
        print_tree(root.right, spaces + " ")
        print(spaces + str(root.data))
        print_tree(root.left, spaces + " ")

def lca(root, v1, v2):
    if contains(root, v1) and contains(root, v2):
        left = lca(root.left, v1, v2)
        right = lca(root.right, v1, v2)

        if left is not None:
            return left
        elif right is not None:
            return right

        return root
    else:
        return None

def main():
    root = None
    root = insert(root, 4)
    root = insert(root, 2)
    root = insert(root, 3)
    root = insert(root, 1)
    root = insert(root, 7)
    root = insert(root, 6)

    print_tree(root, "")

    print()
    print(lca(root, 1, 7).data)

if __name__ == "__main__":
    main()

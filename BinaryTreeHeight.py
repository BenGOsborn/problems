class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        root = Node(data)
    else:
        if data <= root.data:
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

def print_tree(root, spaces):
    if root:
        print_tree(root.right, spaces + " ")
        print(spaces + str(root.data))
        print_tree(root.left, spaces + " ")

def height(root, _height):
    if root is None or (root.left is None and root.right is None):
        return _height;
    else:
        return max(height(root.left, _height + 1), height(root.right, _height + 1))

def main():
    root = None
    root = insert(root, 3)
    root = insert(root, 5)
    root = insert(root, 2)
    root = insert(root, 1)
    root = insert(root, 4)
    root = insert(root, 6)
    root = insert(root, 7)

    print_tree(root, "")

    print()
    print(height(root, 0))

if __name__ == "__main__":
    main()
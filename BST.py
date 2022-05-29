# Create a binary search tree
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

def print_tree(root, spaces):
    if root:
        print_tree(root.left, spaces + " ")
        print(spaces + str(root.data))
        print_tree(root.right, spaces + " ")

def main():
    root = None
    root = insert(root, 5)
    root = insert(root, 4)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 1)
    print_tree(root, "")

if __name__ == "__main__":
    main()
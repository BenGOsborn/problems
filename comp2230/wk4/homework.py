# 11

def enqueue(q, item, max_size):
    if len(q) == max_size:
        return False

    q.append(item)

    return True

# 12

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(parent, root):
    if not root:
        return
    
    reverse_list(root, root.next)

    root.next = parent

# Worst case is O(N) where there are N nodes in the list

# 13

# To implement a queue using a priority queue (a max heap), we simply need to have a key we assign to each item that gets increasingly more negative to thus be smaller, to signify that newer items have less priority than older items. We will also do this using an indirect heap.
# e.g.

# Keys: [-1, -2, -3]
# Into: [1, 2, 3]
# Outof: [1, 2, 3]

# Accessor: {1: elem1, 2: elem2, 3: elem3}

# 14

# Postorder runtime:
# - O(N) for upper bound
# - ohm(N) for lower bound
# Thus we have 0(N) where n is the number of nodes in the tree. This is because we have to visit each node in the tree exactly once

# Additonally, we can count it from recursive calls as O(2**h) where h is the height of the tree or O(N)
# We know that O(2**h), and ohm(2**(h - 1) + 1) = O(N) and ohm(N) thereofre = 0(N)

# 15

def num_leaves(root):
    count = 0

    def num_leaves_help(root):
        if not root:
            count += 1
        
        else:
            num_leaves(root.left)
            num_leaves(root.right)
    
    num_leaves_help(root)

    return count

# 16

def is_bst(root):
    if not root:
        return True
    
    if not root.left or not root.right:
        return True

    if root.val > root.left.val and root.val < root.right.val:
        return is_bst(root.left) and is_bst(root.right)

    return False

# 17

def search_tree(root, val):
    if not root:
        return None

    if root.val == val:
        return root
    
    left = search_tree(root.left)
    if left:
        return left

    right = search_tree(root.right)
    if right:
        return right
    
    return None
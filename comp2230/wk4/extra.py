# 20

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# We will assume that list1 and list2 are both sorted in ascending order


def merge_lists(list1, list2):
    out = ListNode()
    current = out

    while list1 and list2:
        if list1.val < list2.val:
            current.next = ListNode(list1.val)
            list1 = list1.next
        else:
            current.next = ListNode(list2.val)
            list2 = list2.next

        current = current.next

    while list1:
        current.next = ListNode(list1.val)
        current = current.next
        list1 = list1.next

    while list2:
        current.next = ListNode(list2.val)
        current = current.next
        list2 = list2.next

    return out.next

# 21


class Deque:
    def __init__(self):
        self.store = []

    def add_start(self, item):
        self.store.insert(0, item)

    def add_end(self, item):
        self.store.append(item)

    def remove_start(self):
        return self.store.pop(0)

    def remove_end(self):
        return self.store.pop(-1)

# 22

# To implement a stack using a priority queue, we will use an indirect heap once again where the indexes of the heap are
# given indexes that accumulates the more stack elements are put on, to ensure the most recent element added is always at the top of the stack.
# From there, we will get the index and use it in our keys section to access the value that is stored on the stack.

# 23


def post_order(root):
    if not root:
        return ""

    left = post_order(root.left)
    right = post_order(root.right)
    return left + root.val + right

# 24

# I mean it sounds a lot like a BST assuming the datum is the value, however, the fact that it makes the statement of having greater than or equal for both cases is slightly confusing,
# but it would most likely just default to the left first depending on how it was written, therefore it would result in a binary search tree (since it is a binary tree to begin with and
# is ordered properly)

# 25

# Pseudocode
# First we check if the parent has a lesser value than the current node. If it is, we will switch the parent and the item. Since the node below it was less and this new node is greater, this
# hierarchy is maintained. We will keep doing this until the parent of the item is greater than it. At most this could take O(logN) operations as at most we have to traverse the height of the
# heap which is logN


def heap_insert(i, v):
    while i > 1 and v[i] > v[i // 2]:
        temp = v[i]
        v[i] = v[i // 2]
        v[i // 2] = temp

        i = i // 2

# 26


def heap_insert_indirect(val, v, keys):
    v.append(val) 
    i = len(v)

    while i > 1 and keys[val] > keys[v[i // 2]]:
        v[i] = v[i // 2]
        i = i // 2

    v[i] = val

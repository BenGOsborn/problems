# 1

def invert(s):
    temp1 = []
    temp2 = []

    while len(s):
        temp1.append(s.pop(-1))

    while len(temp1):
        temp2.append(temp1.pop(-1))

    while len(temp2):
        s.append(temp2.pop(-1))

x = [1, 2, 3, 4]

invert(x)

print(x)

# 2

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_to_head(start, val):
    if not start:
        return ListNode(val=val)

    return ListNode(val=val, next=start)

out = add_to_head(None, 3)

print(out.val, out.next)

# Worst case = O(1)

# 3

# By appending at the end everytime we have:

# Assuming that we have to copy our items into a new array everytime (or we have to shift the entire elements over) we append one to the array to make the heap we get
# Insertion: 1 + 2 + ... + N = n(n-1) / 2
# Deletion: log(n!)

# Total = n^2 + log(n!) = 0(n^2) as required

# 4

def swap_nodes(root):
    if not root:
        return
    
    temp = root.right
    root.right = root.left
    root.left = temp

    swap_nodes(root.left)
    swap_nodes(root.right)

# 5

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bst_insert(root, val):
    temp = TreeNode(val) 

    if not root:
        return temp

    while True:
        if temp.val < root.val:
            if not root.left:
                root.left = temp
                break
            else:
                root = root.left
        else:
            if not root.right:
                root.right = temp
                break
            else:
                root = root.right

# 6

# i = n = n + 1 = 12
# val = 61

# 1. 12 > 1, 61 > v[12 / 2] = 23
# 1. v[12] = v[6] = 23
# 1. i = 6
# 2. 6 > 1, 61 > v[6 / 2] = 24
# 2. v[6] = v[3] = 24
# 2. i = 3
# 3. 3 > 1, 61 > v[3 / 2] = 71 (FALSE)

# v[3] = 61

# 7

# Smallest element is going to be at the leaves (or possibly the root)
# Second smallest element is guaranteed to be a leaf (as there always are at least 2 leaf nodes except for the root only case)
# Second largest element is going to be second from the top always

# 8

# Insertion from empty (worst case): log(1) + log(2) + log(3) + ... + log(N - 1) + log(N) = log(N!)
# log(N!) < log(N) + log(N) + log(N) + ... + log(N) = Nlog(N), thus O(NlogN)
# https://stackoverflow.com/questions/2095395/is-logn-%CE%98n-logn - good resource for figuring out the splitting
# log(N!) > log(N) + log(N - 1) + ... + log(N / 2) > log(N / 2) + log(N / 2) + ... + log(N / 2) = Nlog(N / 2) = Nlog(N) - Nlog(2) = Nlog(N)
# Thus log(N!) = NlogN which is the worst case insertion time

# 9 (I think this is valid, is it not ?)

# Key array = [18, 24, 71, 5, 22, 23, 66, 32, 8, 25, 27]
# Into = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# Outof = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# 10

# Line 0. parent = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8}

# Line 1. parent = {1: 2, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8}
# Line 2. parent = {1: 2, 2: 2, 3: 4, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8}
# Line 3. parent = {1: 2, 2: 2, 3: 4, 4: 4, 5: 6, 6: 6, 7: 7, 8: 8}
# Line 4. parent = {1: 2, 2: 2, 3: 4, 4: 4, 5: 6, 6: 7, 7: 7, 8: 8}
# Line 5. parent = {1: 2, 2: 2, 3: 4, 4: 4, 5: 6, 6: 7, 7: 8, 8: 8}
# Line 6. parent = {1: 2, 2: 2, 3: 4, 4: 8, 5: 6, 6: 7, 7: 8, 8: 8}
# Line 7. parent = {1: 2, 2: 2, 3: 4, 4: 8, 5: 6, 6: 7, 7: 8, 8: 2}
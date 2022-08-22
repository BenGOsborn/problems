class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Return the kth to last elements from the linked list (we need to find the node k elements from the end)
# - Recursively call a function on the next node in the linked list which stores the progressive count of the element
# - Once we hit the end, record the size of the list, then recurse back up until we get to the stored counter for that node which matches what is given

def helper(head, k, count):
    current = count + 1

    size, node = -1, None

    if head.next is not None:
        size, node = helper(head.next, k, count)
    else:
        size, node = current, None

    if node is None:
        if current == size - k:
            node = head

    return size, node


def kth_to_last(head, k):
    if head is None:
        return

    return helper(head, k, 0)[1]

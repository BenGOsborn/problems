class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

# Partition the values of a linked list around the values of a given partition x
# Intuitively, this problem seems like it is going to be far easier to tackle using a doubly linked list, let us assume we are given a sentinel doubly linked list
# - Create two pointers, one at the start and one at the end
# - Iterate through the list until we find a pair where the left pointer has a value greater than the partition, and the right pointer has a value less than, in which we will swap these elements
# - We will repeat this process until the pointers land on the same node
# Time: O(n) | Space: O(1)

# We will assume that the partition value is guaranteed to be in the list


def swap_nodes(node1, node2):
    temp_val = node1.val
    temp_next = node1.next
    temp_prev = node1.prev

    node1.val = node2.val
    node1.next = node2.next
    node1.prev = node2.prev
    node2.val = temp_val
    node2.next = temp_next
    node2.prev = temp_prev


def partition_list(head, p_val):
    curr_l = head.next
    curr_r = head.prev

    while curr_l is not curr_r:
        if curr_l > p_val and curr_r < p_val:
            swap_nodes(curr_l, curr_r)

            curr_l = curr_l.next
            if curr_l is curr_r:
                break

            curr_r = curr_r.prev

        elif curr_l > p_val:
            curr_r = curr_r.prev

        elif curr_r < p_val:
            curr_l = curr_l.next

        else:
            curr_l = curr_l.next
            if curr_l is curr_r:
                break

            curr_r = curr_r.prev

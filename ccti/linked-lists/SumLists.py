class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Algorithm (backward)
# - Loop through each element in the list and add the sums of the elements to a new linked list
# - If the element in the list exceeds 9, then we will set it to zero and add the modulus to the next element in the list


# Algorithm (forward)
# - We could resursively loop through and do the previous operation
# - We would need to add to the head of the out list instead of the tail
# OR we could just use the first algorithm and reverse it initially


# Algorithm (reverse list)
# - Iterate through until we get to the end
# - Get the end node and return it back to the top (the new head)
# - Set the new nodes next value to be the previous node sent through


def reverse(head):
    if head is None or head.next is None:
        return head

    out = reverse(head.next)

    head.next.next = head

    return out


def sum_lists_backward(list1, list2):
    out = ListNode(0)
    current = out

    while list1 is not None or list2 is not None:
        if list1 is not None:
            current.val += list1.val
        if list2 is not None:
            current.val += list2.val

        current.next = ListNode(0)

        if current.val >= 10:
            current.next.val = current.val % 10
            current.val = 0

        current = current.next

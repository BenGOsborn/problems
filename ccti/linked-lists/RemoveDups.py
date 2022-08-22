class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Assume that we are simply just removing nodes that result in a duplicate, so we end up with a list of unique values
# - Loop through the linked list and store the values for nodes in a hashmap
# - If we have already seen the value before, then flag it and remove it for each node in the array
# - At the end, do another sweep through the list and remove all of the nodes that contained duplicates
# Time: O(n) | Space: O(n)


def remove_dups(head):
    new_head = ListNode()
    new_head.next = head
    head = new_head

    seen = {}
    duplicated = {}

    current = head

    # First pass
    while current.next is not None:
        if current.next.val in seen:
            current.next = current.next.next
            duplicated[current.next.val] = True
            continue

        seen[current.next.val] = True

        current = current.next

    # Second pass
    current = head

    while current.next is not None:
        if current.next.val in duplicated:
            current.next = current.next.next
            continue

        current = current.next

    return head.next

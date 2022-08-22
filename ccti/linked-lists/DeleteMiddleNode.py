class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Delete the node in the middle of a linked list (guaranteed to not be first or last) whilst maintaining the list from only the node that needs to be deleted
# - We cannot delete the current node in the list as it would break the previous chain, therefore, we have to change its value
# - Therefore, we will delete the next node, and replace the current nodes data with the next nodes data
# Time: O(n) | Space: O(n)


def delete_middle_node(head):
    head.val = head.next.val
    head.next = head.next.next

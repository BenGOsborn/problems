class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Check if the values provided in the linked list create a palindrome
# Algorithm:
# - Recursively iterate through the list. On the forward pass, record the finished string, and then on the backwards pass, record the string again
# - At the end, we will compare the two strings generated
# Time: O(n) | Space: O(1)

def helper(head, seen_forward):
    if not head:
        return seen_forward, ""

    out1, out2 = helper(head.next, seen_forward + head.val)

    return out1, out2 + seen_forward


def is_palindrome(head):
    if not head:
        return True

    out1, out2 = helper(head, "")

    return out1 == out2

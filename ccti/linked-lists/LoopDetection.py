class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Detect if a linked list contains a cycle
# Algorithm 1
# - Loop through the list and mark each item as seen
# - If we encounter an element that we have already seen before, we know that a cycle exists
# - If we get to the end of the list, we know it is cycle free
# Time: O(n) | Space: O(n) (but can we do better... ?)
# Algorithm 2 (Floyd's cycle finding algorithm)
# - Loop through the list with one slow and one fast pointer
# - If the fast pointer gets to the end of the list, we know there is no cycle
# - Otherwise if the slow and fast pointer intersect, we have found a cycle


def loop_detection(head):
    pass

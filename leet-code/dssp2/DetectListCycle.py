# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        seen = {}

        while head:
            if head in seen:
                return head
            
            seen[head] = True

            head = head.next

        return None
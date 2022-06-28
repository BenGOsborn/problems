# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        seen = {}

        seen[head] = True

        while head != None and head.next != None:
            head = head.next
            
            if head in seen:
                return True

            seen[head] = True

        return False
        
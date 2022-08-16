# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        temp_head = ListNode()
        temp_head.next = head

        ptr_current = temp_head
        ptr_next = temp_head.next

        seen = False

        while (ptr_next and ptr_next.next) or seen:
            if ptr_next.next and ptr_current.next.val == ptr_next.next.val:
                seen = True
            else:
                if seen:
                    ptr_current.next = ptr_next.next
                    seen = False
                else:
                    ptr_current = ptr_next

            ptr_next = ptr_next.next

        return temp_head.next;
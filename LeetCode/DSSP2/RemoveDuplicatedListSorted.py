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
        ptr_next = temp_head

        seen_counter = 0

        while ptr_next and ptr_next.next:
            if ptr_current.next.val == ptr_next.next.val:
                seen_counter += 1
            else:
                if seen_counter > 1:
                    ptr_current.next = ptr_next.next

                ptr_current = ptr_next
                seen_counter = 1

            ptr_next = ptr_next.next

        return temp_head.next;
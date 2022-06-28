class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head):
    if head != None:
        print(head.val)
        print_list(head.next)

head_0 = ListNode(7)
head_1 = ListNode(7)
head_2 = ListNode(7)
head_3 = ListNode(7)

head_1.next = head_0
head_2.next = head_1
head_3.next = head_2

print_list(head_3)

class Solution:
    def removeElements(self, head, val):
        while head != None:
            if head.val == val:
                head = head.next
            else:
                break

        head_ptr = head

        while head_ptr != None and head_ptr.next != None:
            if head_ptr.next.val == val:
                head_ptr.next = head_ptr.next.next
            else:
                head_ptr = head_ptr.next

        return head

out = Solution().removeElements(head_3, 7)

print()

print_list(out)
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
head_2 = ListNode(3)
head_3 = ListNode(4)

head_1.next = head_0
head_2.next = head_1
head_3.next = head_2

print_list(head_3)

class Solution:
    def deleteDuplicates(self, head):
        current = head

        while current != None and current.next != None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head

print()
print_list(Solution().deleteDuplicates(head_3))
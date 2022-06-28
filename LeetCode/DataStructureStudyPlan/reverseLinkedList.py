class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head):
    if head != None:
        print(head.val)
        print_list(head.next)

head_1_0 = ListNode(4)
head_1_1 = ListNode(3)
head_1_2 = ListNode(2)
head_1_3 = ListNode(1)

head_1_1.next = head_1_0
head_1_2.next = head_1_1
head_1_3.next = head_1_2

class Solution:
    def reverseList(self, head):
        pass
        
print_list(head_1_3)
print()
print_list(Solution().reverseList(head_1_3))
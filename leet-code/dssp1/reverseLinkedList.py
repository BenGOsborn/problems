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
    # def reverse(self, head, storage):
    #     if head == None:
    #         return
        
    #     temp = storage.next
    #     storage.next = ListNode()
    #     storage.next.val = head.val
    #     storage.next.next = temp

    #     self.reverse(head.next, storage)

    # def reverseList(self, head):
    #     storage = ListNode()

    #     if head != None:
    #         self.reverse(head, storage)

    #     return storage.next

    def reverseList(self, head):
        storage = ListNode()

        stack = []

        while head != None:
            stack.append(head.val)
            head = head.next

        while len(stack) > 0:
            temp = storage.next
            storage.next = ListNode()
            storage.next.val = stack.pop(0)
            storage.next.next = temp

        return storage.next
        
print_list(head_1_3)
print()
print_list(Solution().reverseList(head_1_3))
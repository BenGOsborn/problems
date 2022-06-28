class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head):
    if head != None:
        print(head.val)
        print_list(head.next)

head_0_0 = ListNode(4)
head_0_1 = ListNode(3)
head_0_2 = ListNode(2)
head_0_3 = ListNode(1)

head_0_1.next = head_0_0
head_0_2.next = head_0_1
head_0_3.next = head_0_2

# print_list(head_0_3)

head_1_0 = ListNode(4)
head_1_1 = ListNode(3)
head_1_2 = ListNode(2)
head_1_3 = ListNode(1)

head_1_1.next = head_1_0
head_1_2.next = head_1_1
head_1_3.next = head_1_2

# print_list(head_1_3)

class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 == None and list2 == None:
            return None

        sentinel = ListNode()
        current = sentinel

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                temp = list1.next
                list1.next = None

                current.next = list1
                list1 = temp
            else:
                temp = list2.next
                list2.next = None

                current.next = list2
                list2 = temp

            current = current.next

        while list1 != None:
            temp = list1.next
            list1.next = None

            current.next = list1
            list1 = temp

            current = current.next

        while list2 != None:
            temp = list2.next
            list2.next = None

            current.next = list2
            list2 = temp

            current = current.next

        return sentinel.next

out = Solution().mergeTwoLists(head_0_3, head_1_3)
print_list(out)
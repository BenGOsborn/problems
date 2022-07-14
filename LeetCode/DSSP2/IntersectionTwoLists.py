# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        pointer_a = headA
        pointer_b = headB

        while pointer_a and pointer_b and pointer_a != pointer_b:
            pointer_a = pointer_a.next
            pointer_b = pointer_b.next

            if pointer_a == pointer_b:
                return pointer_b

            if not pointer_a:
                pointer_a = headB

            if not pointer_b:
                pointer_b = headA

        return pointer_a
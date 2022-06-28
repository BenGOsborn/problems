class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        out = None
        out_ptr = out # **** I don't know if this is going to continue tracking it

        # **** This is actually really annoying to deal with...

        while list1 != None and list1.next != None and list2 != None and list2.next != None:
            pass

        while list1 != None and list1.next != None:
            pass

        while list2 != None and list2.next != None:
            pass

        return None
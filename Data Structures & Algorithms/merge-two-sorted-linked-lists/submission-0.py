# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        c1 = list1
        c2 = list2

        while c1 and c2:
            v1 = c1.val
            v2 = c2.val
            if v1 <= v2:
                curr.next = c1
                c1 = c1.next
            else:
                curr.next = c2
                c2 = c2.next
            curr = curr.next

        if c1:
            curr.next = c1
        if c2:
            curr.next = c2
        return head.next
        
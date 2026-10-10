# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def printList(self, head):
        while head:
            print(str(head.val) + "->", end=" ")
            head = head.next
        print("None")
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Find mid point of linked list
        #Consider odd/even sized list
        slow = head
        fast = head.next if head else None
        if not fast: return
        old = None

        while (fast):
            old = slow
            slow = slow.next
            fast = fast.next
            fast = fast.next if (fast) else None

        old.next = None

        #mid pointer is at slow, we want to reverse the second half of the linked list
        prev = None
        curr = slow
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        second = prev
        # first = head
        curr = head
        # self.printList(first)
        # self.printList(second)
        # self.printList(head)
        # self.printList(curr)

        while (curr and second):
            nextNode = curr.next
            curr.next = second
            curr = curr.next
            second = nextNode

        if second:
            curr.nexr = second


        



        
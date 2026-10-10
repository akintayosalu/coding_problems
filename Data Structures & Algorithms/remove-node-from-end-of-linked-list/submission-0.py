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

    def getLength(self, head):
        curr = head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        return count

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = self.getLength(head)
        index = size-n

        currCount = 0
        curr = head
        dummyNode = ListNode()
        behind = dummyNode
        dummyNode.next = curr

        while currCount <= index:
            nextNode = curr.next
            if currCount == index:
                behind.next = nextNode
                break
            else:
                behind = curr
            curr = nextNode
            currCount += 1

        return dummyNode.next

        
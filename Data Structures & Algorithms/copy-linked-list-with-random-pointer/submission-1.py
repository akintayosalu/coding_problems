"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #first pass to make copies
        nodeDict = dict()
        curr = head
        while curr:
            newNode = Node(curr.val)
            nodeDict[curr] = newNode
            curr = curr.next
        
        #second pass to assign random pointer for each copy
        curr = head
        while curr:
            currCopy = nodeDict[curr]
            currCopy.next = nodeDict[curr.next] if curr.next else None
            currCopy.random = nodeDict[curr.random] if curr.random else None
            curr = curr.next

        return nodeDict[head] if head else None

        
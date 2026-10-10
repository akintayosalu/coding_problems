# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balance(self, root):
        if not root:
            return (True,0)
        
        lBalance, lHeight = self.balance(root.left)
        rBalance, rHeight = self.balance(root.right)
        isBalance = lBalance and rBalance and (abs(lHeight-rHeight) < 2)
        return (isBalance, 1 + max(lHeight, rHeight))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isB, _ = self.balance(root)

        return isB
        
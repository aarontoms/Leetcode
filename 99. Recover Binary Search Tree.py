# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev=first=second=None

        def inorder(node):
            nonlocal prev, first, second
            if not node:
                return

            inorder(node.left)
            
            if prev and prev.val > node.val:
                if not first:
                    first=prev
                second=node
            prev=node

            inorder(node.right)        
        
        inorder(root)
        first.val, second.val = second.val, first.val
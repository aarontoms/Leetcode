# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        def dfs(node, total):
            if not node:
                return
            total = total*10 + node.val

            if not node.left and not node.right:
                self.total += total
                return
            
            dfs(node.left, total)
            dfs(node.right, total)
        
        dfs(root, 0)
        return self.total
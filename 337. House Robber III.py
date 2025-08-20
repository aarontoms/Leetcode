# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import lru_cache
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @lru_cache(None)
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
                
            rob = node.val + (
                (dfs(node.left.left) if node.left else 0) +
                (dfs(node.left.right) if node.left else 0) +
                (dfs(node.right.left) if node.right else 0) +
                (dfs(node.right.right) if node.right else 0)
            )

            skip = left+right
            return max(rob, skip)

        return dfs(root) 
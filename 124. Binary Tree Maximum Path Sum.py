# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.mx = float("-inf")
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            mx = node.val+max(left,right, left+right, 0)
            if mx > self.mx:
                self.mx = mx
            return node.val+max(left,right, 0)

        dfs(root)
        return self.mx
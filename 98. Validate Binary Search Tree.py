# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, minbound, maxbound):
            if not root:
                return True
            if not (minbound < root.val < maxbound):
                return False

            if root.left and not dfs(root.left, minbound, root.val):
                return False
            if root.right and not dfs(root.right, root.val, maxbound):
                return False

            return True
        
        return dfs(root, float("-inf"), float("inf"))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        
        def dfs(node, sm, path):
            if not node:
                return
            sm+=node.val
            path.append(node.val)
            if not node.left and not node.right:
                if sm==targetSum:
                    res.append(path)
                return
            dfs(node.left, sm, path[:])
            dfs(node.right, sm, path[:])
            path.pop()        
        dfs(root, 0, [])
        return res
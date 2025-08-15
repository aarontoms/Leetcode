# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def symm(lefttree, righttree):
            if not lefttree and not righttree:
                return True
            if not lefttree or not righttree or lefttree.val!=righttree.val:
                return False

            return (
                symm(lefttree.left, righttree.right) and 
                symm(lefttree.right, righttree.left)
            )
        
        return symm(root.left, root.right)
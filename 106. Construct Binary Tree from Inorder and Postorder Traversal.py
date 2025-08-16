# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        i=0
        n=len(postorder)-1
        pos = {val:ind for ind,val in enumerate(inorder)}
        def build(left, right):
            nonlocal i
            if left>right:
                return
            root = TreeNode(postorder[n-i])
            pivot = pos[postorder[n-i]]
            i+=1
            root.right = build(pivot+1, right)
            root.left = build(left, pivot-1)
            return root

        return build(0, n)
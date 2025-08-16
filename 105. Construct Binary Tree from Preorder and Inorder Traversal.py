# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {x: i for i,x in enumerate(inorder)}
        i=0
        def build(left, right):
            nonlocal i
            if left>right:
                return

            root = TreeNode(preorder[i])
            pivot = pos[preorder[i]]
            i+=1
            root.left = build(left, pivot-1)
            root.right = build(pivot+1, right)
            return root

        return build(0, len(preorder)-1)
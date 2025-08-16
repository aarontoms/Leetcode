# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def build(preorder, inorder):
            if not preorder or not inorder:
                return
            root = TreeNode(preorder[0])
            pivot = inorder.index(preorder[0])
            root.left = build(preorder[1:1+pivot], inorder[:pivot])
            root.right = build(preorder[pivot+1:], inorder[pivot+1:])

            return root

        return build(preorder[:], inorder[:])
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        def middle(left, right):
            slow=fast=left
            while fast!=right and fast.next!=right:
                slow = slow.next
                fast = fast.next.next
            return slow

        def build(left, right):
            if left==right:
                return
            pivot = middle(left, right)
            root = TreeNode(pivot.val)
            root.left = build(left, pivot)
            root.right = build(pivot.next, right)
            return root

        return build(head, None)
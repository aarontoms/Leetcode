# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res=[]
        queue=deque()
        queue.append(root)
        while queue:
            level, temp = [], []
            for _ in range(len(queue)):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            res.append(level)
            queue=deque(temp[::-1])
            if not queue:
                break
            temp,level=[],[]
            for _ in range(len(queue)):
                node=queue.popleft()
                level.append(node.val)
                if node.right:
                    temp.append(node.right)
                if node.left:
                    temp.append(node.left)
            queue=deque(temp[::-1])
            res.append(level)
        return res
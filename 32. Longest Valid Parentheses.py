class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left=right=count=0

        for ch in s:
            if ch=="(":
                left+=1
            else:
                right+=1
            
            if right>left:
                left=right=0
            elif left==right:
                count=max(count, left+right)
        
        left=right=0
        for ch in reversed(s):
            if ch=="(":
                left+=1
            else:
                right+=1
            
            if left>right:
                left=right=0
            elif left==right:
                count=max(count, left+right)
            
        return count
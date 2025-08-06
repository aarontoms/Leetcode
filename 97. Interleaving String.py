class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m+n!=len(s3):
            return False
        memo={}

        def backtrack(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i+j==len(s3):
                memo[(i, j)]=True
                return True
            
            valid=False
            if i<m and s1[i]==s3[i+j]:
                valid |= backtrack(i+1, j)
            if j<n and s2[j]==s3[i+j]:
                valid |= backtrack(i, j+1)
            
            memo[(i, j)]=valid
            return valid            

        return backtrack(0, 0)
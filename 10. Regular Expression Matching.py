from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        @lru_cache(None)
        def backtrack(i, j):
            if i>=m and j>=n:
                return True
            if j>=n:
                return False
            
            match = i<m and (p[j]=="." or s[i]==p[j])
            if j+1<n and p[j+1]=="*":
                return (match and backtrack(i+1, j) or backtrack(i, j+2))
            if match:
                return backtrack(i+1, j+1)

            return False

        return backtrack(0, 0)

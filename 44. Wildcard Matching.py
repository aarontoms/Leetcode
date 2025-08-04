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

            if i<m and (p[j]=="?" or s[i]==p[j]):
                return backtrack(i+1, j+1)
            if p[j]=="*":
                return ((i<m and backtrack(i+1, j)) or backtrack(i, j+1))
            return False
            
        return backtrack(0, 0)
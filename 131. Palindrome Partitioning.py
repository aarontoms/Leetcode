from functools import lru_cache

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        n=len(s)

        @lru_cache(None)
        def palindrome(i, j):
            while i<=j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True

        def backtrack(start, pal):
            if start==n:
                res.append(pal[:])
                return

            for end in range(start, n):
                if palindrome(start, end):
                    pal.append(s[start:end+1])
                    backtrack(end+1, pal)
                    pal.pop()

        backtrack(0, [])
        return res
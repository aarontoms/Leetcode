from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words=set(wordDict)
        n=len(s)
        
        @lru_cache(None)
        def backtrack(start):
            if start>=n:
                return True
            
            res=False
            for end in range(start, n):
                if s[start:end+1] in words:
                    res |= backtrack(end+1)
            
            return res

        return backtrack(0)
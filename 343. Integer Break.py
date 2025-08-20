from functools import lru_cache

class Solution:
    def integerBreak(self, n: int) -> int:
        
        @lru_cache(None)
        def backtrack(num):
            if num==2:
                return num

            res=0
            for i in range(1, num):
                res = max(res, i*max(num-i, backtrack(num-i)))
            return res

        resmax = 0
        for i in range(1, n):
            resmax = max(resmax, i*max(n-i, backtrack(n-i)))
        return resmax
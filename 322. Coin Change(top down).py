from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @lru_cache(None)
        def backtrack(rem):
            if rem<0:
                return float("inf")
            if rem==0:
                return 0
            
            res = float("inf")
            for coin in coins:
                res = min(res, 1+backtrack(rem-coin))
            return res

        least = backtrack(amount)
        if least == float("inf"):
            return -1
        return least
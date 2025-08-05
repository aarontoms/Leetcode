class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}

        def backtrack(n):
            if n<2:
                return 1
            if n in memo:
                return memo[n]

            memo[n] = backtrack(n-1)+backtrack(n-2)
            return memo[n]
        
        return backtrack(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        n+=1
        dp=[0]*n
        dp[0]=1

        for i in range(1, n):
            dp[i] += dp[i-1]
            if i>=2:
                dp[i] += dp[i-2]

        return dp[-1]
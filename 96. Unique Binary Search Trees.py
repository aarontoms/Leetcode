class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = [0]*(n+1)
        dp[0]=dp[1]=1

        for node in range(2, n+1):
            for i in range(1, n+1):
                dp[node] += dp[i-1]*dp[n-i]
        return dp[n]
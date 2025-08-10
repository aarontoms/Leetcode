class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)

        dp = [[0]*n for _ in range(k+1)]

        for t in range(1, k+1):
            maxdiff = -prices[0]
            for d in range(1, n):
                dp[t][d] = max(prices[d]+maxdiff, dp[t][d-1])
                maxdiff = max(maxdiff, dp[t-1][d]-prices[d])

        return dp[k][n-1]
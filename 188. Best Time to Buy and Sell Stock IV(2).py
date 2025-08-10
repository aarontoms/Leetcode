from math import inf

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)

        buy=[-inf]*k
        sell=[-inf]*k

        for price in prices:
            buy[0] = max(buy[0], -price)
            sell[0] = max(sell[0], price+buy[0])
            for i in range(1, k):
               buy[i] = max(buy[i], sell[i-1]-price)
               sell[i] = max(sell[i], buy[i]+price)

        return sell[-1]
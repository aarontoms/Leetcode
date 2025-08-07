class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float("inf")
        maxprof = 0
        for price in prices:
            if price<minprice:
                minprice = price
            if price-minprice>maxprof:
                maxprof = price-minprice
        return maxprof
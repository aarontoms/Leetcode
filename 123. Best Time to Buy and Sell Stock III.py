class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        leftprofs=[0]*n
        rightprofs=[0]*n
        minprice, maxprice = prices[0], prices[-1]

        for i in range(1, n):
            if prices[i]-minprice > leftprofs[i-1]:
                leftprofs[i] = prices[i]-minprice 
            else:
                leftprofs[i] = leftprofs[i-1] 
            if prices[i]<minprice:
                minprice=prices[i]
        
        for i in range(n-2, -1, -1):
            if maxprice-prices[i] > rightprofs[i+1]:
                rightprofs[i]=maxprice-prices[i]
            else:
                rightprofs[i]=rightprofs[i+1]
            if prices[i]>maxprice:
                maxprice=prices[i]

        maxprof=0
        for i in range(n):
            if leftprofs[i]+rightprofs[i]>maxprof:
                maxprof=leftprofs[i]+rightprofs[i]
        return maxprof
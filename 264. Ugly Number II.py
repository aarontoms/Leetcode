class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        dp = [1]
        i2=i3=i5=0

        while n>len(dp):
            fact2 = dp[i2]*2
            fact3 = dp[i3]*3
            fact5 = dp[i5]*5
            nextval = min(fact2, fact3, fact5)

            if nextval==fact2:
                i2+=1
            if nextval==fact3:
                i3+=1
            if nextval==fact5:
                i5+=1
            dp.append(nextval)

        return dp[n-1]
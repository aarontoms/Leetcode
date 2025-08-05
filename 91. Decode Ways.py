class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        memo={}

        def backtrack(i):
            if i in memo:
                return memo[i]

            if i>=n:
                return 1
            if s[i]=="0":
                return 0
            
            count=backtrack(i+1)
            if i+1<n and 9<int(s[i]+s[i+1])<=26:
                count+=backtrack(i+2)
            memo[i]=count
            return count

        return backtrack(0)
class Solution:
    def minCut(self, s: str) -> int:
        n=len(s)
        dp=[i-1 for i in range(n+1)]
        pal=[[False]*n for _ in range(n)]

        for end in range(n):
            for start in range(end+1):
                if s[start]==s[end] and (end-start<=1 or pal[start+1][end-1]):
                    pal[start][end]=True
                    if dp[end+1]>dp[start]+1:
                        dp[end+1]=dp[start]+1

        return dp[n]
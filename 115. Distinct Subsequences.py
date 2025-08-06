class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        memo={}

        def backtrack(i ,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if j==n:
                return 1
            elif i==m or m-i<n-j:
                return 0

            count=0
            if s[i]==t[j]:
                count+=backtrack(i+1, j+1)
            count+=backtrack(i+1, j)

            memo[(i,j)]=count
            return count

        return backtrack(0, 0)
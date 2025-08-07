class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo={}

        def dfs(i, j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i==len(triangle)-1:
                memo[(i,j)]=triangle[i][j]
                return triangle[i][j]

            s=min(dfs(i+1, j), dfs(i+1, j+1))
            memo[(i,j)] = s+triangle[i][j]
            return s+triangle[i][j]

        return dfs(0, 0)
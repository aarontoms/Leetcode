class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo={}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            left = right = top = bottom = 0
            if i>0 and matrix[i][j]>matrix[i-1][j]:
                left = dfs(i-1, j)
            if i<m-1 and matrix[i][j]>matrix[i+1][j]:
                right = dfs(i+1, j)
            if j>0 and matrix[i][j]>matrix[i][j-1]:
                top = dfs(i, j-1)
            if j<n-1 and matrix[i][j]>matrix[i][j+1]:
                bottom = dfs(i, j+1)
            
            memo[(i, j)] = 1+max(left, right, top, bottom)
            return memo[(i, j)]
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        
        return res
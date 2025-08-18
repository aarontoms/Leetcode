class Solution:
    def numSquares(self, n: int) -> int:
        i=1
        squares=[]
        while i*i<=n:
            squares.append(i*i)
            i+=1

        memo = {}

        def backtrack(num):
            if num in memo:
                return memo[num]

            if num==0:
                return 0

            res=float("inf")
            for sq in squares:
                if sq<=num:
                    res = min(res, 1+backtrack(num-sq))

            memo[num] = res
            return res

        return backtrack(n)
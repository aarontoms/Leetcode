class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        d1 = set()
        d2 = set()

        def backtrack(depth, cols, d1, d2):
            if depth==n:
                return 1

            res = 0
            for col in range(n):
                if col not in cols and (depth-col) not in d1 and (depth+col) not in d2:
                    cols.add(col)
                    d1.add(depth-col)
                    d2.add(depth+col)
                    res += backtrack(depth+1, cols, d1, d2)
                    cols.remove(col)
                    d1.remove(depth-col)
                    d2.remove(depth+col)
            return res

        return backtrack(0, cols, d1, d2)
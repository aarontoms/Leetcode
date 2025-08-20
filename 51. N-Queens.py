class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        d1 = set()
        d2 = set()
        paths, res = [], []

        def backtrack(depth, cols, d1, d2, path):
            if depth==n:
                paths.append(path[:])
                return

            for i in range(n):
                if i not in cols and (depth-i) not in d1 and (depth+i) not in d2:
                    cols.add(i)
                    d1.add(depth-i)
                    d2.add(depth+i)
                    path.append(i)
                    backtrack(depth+1, cols, d1, d2, path)
                    path.pop()
                    cols.remove(i)
                    d1.remove(depth-i)
                    d2.remove(depth+i)

        backtrack(0, cols, d1, d2, [])
        
        for path in paths:
            temp = []
            for col in path:
                temp.append("."*col + "Q" + "."*(n-col-1))
            res.append(temp[:])
        
        return res
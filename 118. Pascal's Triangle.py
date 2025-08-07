class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return[[1]]
        i=1
        res=[[1]]
        for i in range(1, numRows):
            newrow=[1]
            for t in range(1, i):
                newrow.append(res[i-1][t-1]+res[i-1][t])
            newrow.append(1)
            res.append(newrow)

        return res
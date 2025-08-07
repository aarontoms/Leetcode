class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[1]
        if rowIndex==1:
            res.append(1)
            return res

        for _ in range(rowIndex):
            newrow=[1]
            for j in range(1, len(res)):
                newrow.append(res[j-1]+res[j])
            newrow.append(1)
            res=newrow[:]
            print(res)

        return res
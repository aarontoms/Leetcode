class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        
        row = [""] * numRows
        rowNum, down = 0, False
        for char in s:
            row[rowNum] += char
            if rowNum==0 or rowNum==numRows-1:
                down = not down
            rowNum = rowNum+1 if down else rowNum-1

        return "".join(row)
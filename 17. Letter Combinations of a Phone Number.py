class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = [""]

        if not digits:
            return []

        for digit in digits:
            letters = d[digit]
            temp=[]
            for letter in letters:
                for comb in res:
                    comb+=letter
                    temp.append(comb)
            res=temp
        
        return res
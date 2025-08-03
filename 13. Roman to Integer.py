class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res=0
        prev=1000

        for ch in s:
            val = symbols[ch]
            if prev<val:
                res-=2*prev
            res+=val
            prev=val
                
        return res
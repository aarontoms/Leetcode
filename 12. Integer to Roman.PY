class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        symbol = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        i=12
        res=""

        while num>0:
            while values[i]>num:
                i-=1
            num-=values[i]
            res+=symbol[i]
        
        return res
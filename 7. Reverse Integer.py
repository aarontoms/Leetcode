class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1
        
        num = 0
        temp=-x if x<0 else x

        while temp>0:
            mod = temp % 10
            num = (num*10) + mod
            temp = temp//10
        
        if num<INT_MIN or num>INT_MAX:
            return 0
        return -num if x<0 else num

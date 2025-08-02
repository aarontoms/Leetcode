class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -(2**31)
        INT_MAX = (2**31) - 1
        neg = numstarted = signstarted = False
        n = len(s)
        i = 0
        num=""
        while i<n:
            if(numstarted or signstarted) and s[i]=="  ":
                break
            while i<n and s[i]==" ":
                i+=1

            if i==n:
                break

            if (s[i]=="+" or s[i]=="-"):
                if signstarted:
                    break
                if s[i] == "+":
                    neg = False
                elif s[i] == "-":
                    neg = True
                signstarted = True
                i+=1
                if i==n:
                    break

            if s[i].isdigit():
                numstarted = True
                signstarted = True
                while  i<n and s[i].isdigit():
                    num+=s[i]
                    print(num)
                    i+=1
            else:
                break

        if not num:
            return 0
        num = int(num)
        if num>INT_MAX:
            return INT_MIN if neg else INT_MAX
        return -num if neg else num
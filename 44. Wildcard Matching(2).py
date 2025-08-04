class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        i=j=0
        star=-1

        while i<m:
            if j<n and (p[j]=="?" or s[i]==p[j]):
                i+=1
                j+=1
            elif j<n and p[j]=="*":
               star=j
               match=i
               j+=1
            elif star!=-1:
                j=star+1
                match+=1
                i=match
            else:
                return False


        while j<n and p[j]=="*":
            j+=1
        if j==n:
            return True
        return False
class Solution:
    def countDigitOne(self, n: int) -> int:
        count=0
        place=1
        while place<=n:
            low = n - (n//place) * place
            curr = (n//place) % 10
            high = n//(place * 10)
            
            if curr==0:
                count += high * place
            elif curr==1:
                count += high * place+low+1
            else:
                count += (high+1) * place

            place *= 10
        
        return count
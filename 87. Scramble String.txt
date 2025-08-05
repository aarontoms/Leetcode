class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s2)
        memo={}

        def backtrack(a, b):
            if (a,b) in memo:
                return memo[(a,b)]
            if a==b:
                memo[(a,b)] = True
                return True
            if sorted(a) != sorted(b):
                return False

            n=len(a)
            for i in range(1, n):
                if backtrack(a[:i], b[:i]) and backtrack(a[i:], b[i:]):
                    memo[(a,b)] = True
                    return True
                if backtrack(a[:i], b[-i:]) and backtrack(a[i:], b[:-i]):
                    memo[(a,b)] = True
                    return True

            memo[(a,b)] = False
            return False
    
        return backtrack(s1, s2)
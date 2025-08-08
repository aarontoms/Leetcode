class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n=len(s)
        words=set(wordDict)
        res=[]

        def backtrack(start, sentence):
            if start==n:
                res.append(sentence.strip())
                return

            for end in range(start, n):
                if s[start:end+1] in words:
                    backtrack(end+1, sentence+s[start:end+1]+" ")
            
        backtrack(0, "")
        return res
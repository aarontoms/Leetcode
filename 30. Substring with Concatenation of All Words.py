class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words)
        wordlen = n*len(words[0])
        concat, res = [], []

        def backtrack(words, perm):
            if perm not in s:
                return
            if len(words)==0:
                concat.append(perm)
                return
            
            for i in range(len(words)):
                if words[i] in s:
                    backtrack(words[:i]+words[i+1:], perm+words[i])
            
        backtrack(words, "")
        
        for c in concat:
            left,right = 0,wordlen
            while right<=len(s):
                if s[left:right]==c and left not in res:
                    res.append(left)
                left+=1
                right+=1
        return res
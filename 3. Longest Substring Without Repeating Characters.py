class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left=maxlen=0
        chars = set()

        for right in range(n):
            while s[right] in chars:
                chars.remove(s[left])
                left+=1
                
            chars.add(s[right])
            maxlen = max(maxlen, right-left+1)

        return maxlen
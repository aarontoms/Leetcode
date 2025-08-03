class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]

        for word in strs:
            while not word.startswith(common):
                common = common[:-1]
                if common == "":
                    return ""
        
        return common
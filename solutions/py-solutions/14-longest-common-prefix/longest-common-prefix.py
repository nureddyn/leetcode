class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        register = 0
        prefix = min(strs, key=len)
        i = 0
        while i < len(strs) and prefix != "":
            st = strs[i]
            if prefix in st[:len(prefix)]:
                register += 1
                i += 1
            else:
                prefix = prefix[:len(prefix)-1]
                register = 0
                i = 0
        if register == len(strs):
            return prefix
        return ""
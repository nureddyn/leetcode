class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        result = ""
        for i in range(1, len(str1)+1):
            if str1[0:i]*(len(str1)//len(str1[0:i])) == str1 and str1[0:i]*(len(str2)//len(str1[0:i])) == str2:
                result = str1[0:i]
        return result

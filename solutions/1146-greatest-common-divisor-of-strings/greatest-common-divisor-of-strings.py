class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) == 0 or len(str2) == 0:
            return ""
        if len(str1) < len(str2):
            small_str, large_str = str1, str2
        else:
            small_str, large_str = str2, str1
        if large_str == small_str*int(len(large_str)/len(small_str)):
            return small_str
        gcd = ""
        for i in range(1, (len(small_str)//2)+1):
            if (small_str == small_str[0:i]*(len(small_str)//len(small_str[0:i]))
                and large_str == small_str[0:i]*(len(large_str)//len(small_str[0:i]))):
                gcd = small_str[0:i]
        return gcd
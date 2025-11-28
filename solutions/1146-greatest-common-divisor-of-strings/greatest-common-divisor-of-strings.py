class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) == 0 or len(str2) == 0:
            return ""
        if len(str1) < len(str2):
            small_str, large_str = str1, str2
        else:
            small_str, large_str = str2, str1
        for i in range(len(small_str), 0, -1):
            substr = small_str[0:i]
            if (len(large_str) % len(substr) == 0
            and large_str == substr * int(len(large_str)/len(substr))
            and small_str == substr * int(len(small_str)/len(substr))):
                return substr
        return ""

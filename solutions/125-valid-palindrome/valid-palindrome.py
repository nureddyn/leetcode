class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        length = len(s)
        while i < length:
            if s[i].isalnum() == False:
                s = s.replace(s[i], "", 1)
                length -= 1
            else:
                i += 1
        if s == s[::-1]:
            return True
        return False
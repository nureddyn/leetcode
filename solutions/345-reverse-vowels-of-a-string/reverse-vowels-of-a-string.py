class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s)-1
        s = list(s)
        while i < j:
            if self.isVowel(s[i]) and self.isVowel(s[j]):
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp
                i+=1
                j-=1
            else:
                if not self.isVowel(s[i]):
                    i += 1
                if not self.isVowel(s[j]):
                    j -= 1
        s = self.toString(s)
        return s
    def isVowel(self, c: str) -> bool:
        vowels = ['a','e','i','o','u']
        if c.lower() in vowels:
            return True
        return False
    def toString(self, l: list) -> str:
        result = ""
        for i in range(len(l)):
            result = result + l[i]
        return result
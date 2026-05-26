class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 1:
            return s
        i, j = 0, 1
        reversed = ""
        while j < len(s):
            if s[i] == " ":
                i+=1
                j+=1
                continue
            elif s[j] == " ":
                if j == len(s)-1:  
                    reversed = s[i:j]+reversed
                    break
                reversed = " "+s[i:j]+reversed
                i=j+1
                j=i+1
            elif j == len(s)-1:
                reversed = s[i:j+1]+reversed
                break
            else:
                j+=1
        if j == len(s) and s[i] != " ":
            reversed = s[i]+reversed
        if reversed[0] == " ":
            reversed = reversed[1:]
        return reversed
        
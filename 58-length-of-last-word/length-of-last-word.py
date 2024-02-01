class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        reversed_s = s[::-1]
        word_length = 0
        start = False
        for i in range(-1, - len(reversed_s) - 1, -1):
            if s[i] != " ":
                start = True
                word_length += 1
            elif start == True:
                break
        return word_length
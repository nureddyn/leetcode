class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        total_len = len(word1) + len(word2)
        i, j = 0, 0
        for k in range(total_len):
            if i < len(word1):
                if j < len(word2):
                    result = result + word1[i]
                    i += 1
                else:
                    result = result + word1[i:]
                    break
            else:
                if j < len(word2):
                    result = result + word2[j:]
                    break
                break
            if j < len(word2):
                if i < len(word1):
                    result = result + word2[j]
                    j += 1
                    pass
                else:
                    result = result + word2[j:]
                    break
            else:
                if i < len(word1):
                    result = result + word1[j:]
                    break
                break
        return result
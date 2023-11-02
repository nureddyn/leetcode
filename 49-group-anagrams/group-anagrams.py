class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = {}
        for word in strs:
            key_word = "".join(sorted(word))
            if key_word in solution.keys():
                solution[key_word].append(word)
            else:
                solution[key_word] = [word]
        return solution.values()

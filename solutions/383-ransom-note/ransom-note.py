class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        register = {}
        counter = 0
        for letter in ransomNote:
            if letter in register:
                if letter in magazine[register[letter][-1]+1:]:
                    counter += 1
                    register[letter].append(magazine[register[letter][-1]+1:].index(letter) + len(magazine[0:register[letter][-1]+1]))
                else:
                    break
            else:
                if letter in magazine:
                    counter += 1
                    register[letter] = [magazine.index(letter)]
        if counter == len(ransomNote):
            return True
        return False
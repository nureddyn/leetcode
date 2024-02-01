class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        self.s = s
        self.t = t
        result = False
        if len(self.s) == len(self.t) and self.s != self.t:
            result = sorted(self.s) == sorted(self.t)
        else:
            result = self.s == self.t
        return result
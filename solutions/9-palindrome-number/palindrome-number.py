class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = len(str(x))
        counter_up = 1
        for i in range(n):
            if (x < 0 and n == 2) or x // 10**i % 10 != x // 10**(n-counter_up) % 10:
                return False
            counter_up += 1
        return True
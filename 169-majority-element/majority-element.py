class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        register = {}
        for num in nums:
            if str(num) not in register:
                register[str(num)] = 1
            else:
                register[str(num)] += 1
            if register[str(num)] > (n / 2):
                return num
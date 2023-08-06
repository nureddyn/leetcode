class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) >= 1 and len(nums) <= 10**5:
            for number in nums:
                if number < -(10**9) or number > 10**9:
                    return 1
            return len(set(nums)) != len(nums)
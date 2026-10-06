class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        original_nums = nums.copy()
        nums.sort()
        left = 0
        right = len(nums)-1
        while left < right:
            if nums[left]+nums[right] == target:
                values = [nums[left], nums[right]]
                break
            elif nums[left]+nums[right] > target:
                right-=1
            elif nums[left]+nums[right] < target:
                left+=1
        result = [self.search_index(original_nums, values[0]), self.search_index(original_nums, values[1], reverse=True)]
        return result
    def search_index(self, nums, value, reverse=False):
        if reverse == True:
            for i in range(len(nums)-1,-1,-1):
                if nums[i] == value:
                    return i
        for i in range(len(nums)):
            if nums[i] == value:
                return i
        return
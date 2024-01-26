class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for left_index in range(0, len(nums) - 1):
            right_index = left_index + 1
            while right_index < len(nums):
                if nums[left_index] == nums[right_index]:
                    nums.pop(right_index)
                else:
                    right_index += 1
        return len(nums)
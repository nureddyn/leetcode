class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        leftLimit = len(nums) - 1
        rightLimit = len(nums)

        for leftNumber in range(0, leftLimit):
            for rightNumber in range(leftNumber + 1, rightLimit):
                if nums[leftNumber] + nums[rightNumber] == target:
                    return [leftNumber, rightNumber]
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_count = {}
        k = 0
        i = 0
        while i < len(nums):
            if str(nums[i]) not in nums_count:
                nums_count[str(nums[i])] = 1
                k += 1

            elif nums_count[str(nums[i])] < 2:
                nums_count[str(nums[i])] += 1
                k += 1
            elif i < len(nums) - 1:
                for j in range(i+1, len(nums)):
                    if str(nums[j]) not in nums_count or nums_count[str(nums[j])] < 2:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        i -= 1
                        break
            i += 1

        return k
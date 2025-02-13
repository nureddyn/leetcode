class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        log = {}
        nums = sorted(nums, reverse=True)
        for i in range(len(nums)):
            if nums[i] not in log.keys():
                log[nums[i]] = 1
            else:
                log[nums[i]]+=1
        if list(log.keys()) == nums:
            return nums[:k]
        result = []
        count = 0
        keys = list(log.keys())
        values = list(log.values())
        while count < k:
            max_index = values.index(max(values))
            result.append(keys[max_index])
            keys.pop(max_index)
            values.pop(max_index)
            count+=1

        return result
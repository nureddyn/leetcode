class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = 1
        sufix_product = 1
        prefixes = [prefix_product]
        sufixes = [prefix_product]
        for i in range(len(nums)):
            if i > 0:
                prefix_product*=nums[i-1]
                prefixes.append(prefix_product)
        for i in range(len(nums)-1, -1, -1):
            if i < len(nums)-1:
                sufix_product*=nums[i+1]
                sufixes.append(sufix_product)
        answer = []
        for i in range(len(nums)):
            answer.append(prefixes[i]*sufixes[len(nums)-1-i])
        return answer
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        max_candies = max(candies)
        for i in range(len(candies)):
            result.append(candies[i] + extraCandies >= max_candies)
        return result
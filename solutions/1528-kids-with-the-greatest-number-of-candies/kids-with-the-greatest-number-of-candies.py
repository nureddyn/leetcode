class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for i in range(len(candies)):
            result.append(candies[i] + extraCandies >= max(candies))
        return result
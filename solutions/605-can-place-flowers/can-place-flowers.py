class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed_len = len(flowerbed)
        if n == 0:
            return True 
        if flowerbed_len == 1 and flowerbed[0] == 0:
            return True
        if sum(flowerbed) == 0:
            if flowerbed_len % 2 == 0:
                if n > flowerbed_len//2:
                    return False
                return True
            elif flowerbed_len % 2 != 0:
                if n > (flowerbed_len//2)+1:
                    return False
                return True
        if sum(flowerbed[0:2]) == 0:
            flowerbed[0] = 1
            n = n-1
            if n == 0:
                return True
        window = 3
        for i in range(flowerbed_len-window+1):
            if n > 0:
                j = i + window
                if sum(flowerbed[i:j]) == 0:
                    flowerbed[i+1] = 1
                    n = n-1
                elif (j-1 == flowerbed_len-1 and
                    sum(flowerbed[i:j]) == 1 and
                    flowerbed[i+1]+flowerbed[i+2] == 0):
                    flowerbed[i+2] = 1
                    n = n-1
        return n == 0
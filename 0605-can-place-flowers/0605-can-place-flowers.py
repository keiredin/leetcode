class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            prev = i - 1
            nex = i + 1
            if prev >= 0 and nex < len(flowerbed) and flowerbed[prev] == flowerbed[nex] == 0:
                flowerbed[i] = 1
                n -= 1
            elif nex >= len(flowerbed) and flowerbed[prev] == 0:
                flowerbed[i] = 1
                n -= 1
            elif prev < 0 and flowerbed[nex] == 0:
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return n <= 0
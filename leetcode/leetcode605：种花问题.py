class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0 or flowerbed == [0]:
            return True
        if flowerbed == [1]:
            return False
        if flowerbed[0] == 0:
            if flowerbed[1] == 0:
                n -= 1
                if n == 0:
                    return True
                flowerbed[0] = 1
        if flowerbed[-1] == 0:
            if flowerbed[-2] == 0:
                flowerbed[-1] = 1
                n -= 1
                if n == 0:
                    return True
        i = 1
        while i<=len(flowerbed)-3:
            if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] == 0:
                n -= 1
                flowerbed[i+1] = 1
            if n == 0:
                break
            i += 1
        if n == 0:
            return True
        return False
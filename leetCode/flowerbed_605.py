class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        l = len(flowerbed)
        i = 0
        while n > 0 and i < l:
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and \
                    (i == l - 1 or flowerbed[i + 1] == 0):
                n -= 1
                flowerbed[i] = 1
            i += 1
        return n == 0

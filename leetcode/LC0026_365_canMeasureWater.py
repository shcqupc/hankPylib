class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x + y < z:
            return False
        if z == x or z == y:
            return True
        maxcf = x % y
        while maxcf != 0:
            x = y
            y = maxcf
            maxcf = x % y
        if z % y == 0:
            return True
        return False


s = Solution()
print(s.canMeasureWater(3, 5, 4))

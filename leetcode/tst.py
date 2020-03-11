class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A or sum(A) % 3 > 0:
            return False
        s = sum(A) / 3
        bin = 0
        cnt = 0
        for i in A:
            if cnt == 2:
                return True
            bin += i
            if bin == s:
                bin = 0
                cnt += 1
        return False


s = Solution()
print(s.canThreePartsEqualSum([]))
print(s.canThreePartsEqualSum([0, 0, 0, 0]))
print(s.canThreePartsEqualSum([1, -1, 1, -1]))
print(s.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
print(s.canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]))
print(s.canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))

'''
给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。
返回使 A 中的每个值都是唯一的最少操作次数。
'''


class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        sort the list in ascending
        """
        A.sort()
        cnt = 0
        for i in range(1, len(A)):
            if A[i] <= A[i - 1]:
                cnt += A[i - 1] + 1 - A[i]
                A[i] = A[i - 1] + 1
        return cnt


s = Solution()
print(s.minIncrementForUnique([3, 2, 1, 2, 1, 7]))
print(s.minIncrementForUnique([1, 2, 2]))
print(s.minIncrementForUnique([]))

#####################################################
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
#####################################################
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        动态规划 O(N²)
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS_2(self, nums):
        """
        动态规划+二分查找 O(NlogN)
        tails[k] 的值代表长度为k+1子序列的尾部元素值。
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num:
                    j = m
                else:
                    i = m + 1
            tails[i] = nums
            if j == res:
                res += 1
        return res


s = Solution()
print(s.lengthOfLIS([]))
print(s.lengthOfLIS([3, 1, 2]))
print(s.lengthOfLIS([10, 9, 2, 5, 3, 4]))
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(s.lengthOfLIS([7, 1, 8, 9, 3, 4]))

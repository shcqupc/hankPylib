'''
322. 零钱兑换 难度 中等
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。
示例 1:
输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
'''


class Solution(object):
    def coinChange_1(self, coins, amount):
        """
        动态规划：自下而上 - 抄作业
        执行用时 :840 ms, 在所有 Python 提交中击败了84.86%的用户
        内存消耗 :12.2 MB, 在所有 Python 提交中击败了22.61%的用户
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

    def coinChange_2(self, coins, amount):
        """
        贪心 + dfs
        执行用时 :104 ms, 在所有 Python 提交中击败了100.00%的用户
        内存消耗 :12.7 MB, 在所有 Python 提交中击败了15.46%的用户
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        def coinChanging(coins, amount, c_index, count, ans):
            if amount == 0:
                return min(ans, count)
            if c_index == len(coins):
                return ans
            k = amount // coins[c_index]
            while k >= 0 and k + count < ans:
                ans = coinChanging(coins, amount - k * coins[c_index], c_index + 1, count + k, ans)
                k -= 1
            return ans

        if amount == 0:
            return 0
        coins.sort(reverse=True)
        ans = coinChanging(coins, amount, 0, 0, float('inf'))
        return ans if ans != float('inf') else -1


s = Solution()
# print(s.coinChange_2([1, 2, 3], 6))
# print(s.coinChange_2([2], 3))
# print(s.coinChange_2([1, 2, 5], 11))
print(s.coinChange_2([1, 7, 10], 14))

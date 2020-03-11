'''
分糖果 II
输入：candies = 7, num_people = 4
输出：[1,2,3,1]
解释：
第一次，ans[0] += 1，数组变为 [1,0,0,0]。
第二次，ans[1] += 2，数组变为 [1,2,0,0]。
第三次，ans[2] += 3，数组变为 [1,2,3,0]。
第四次，ans[3] += 1（因为此时只剩下 1 颗糖果），最终数组变为 [1,2,3,1]。
'''


class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        n = 0
        a = 0
        ln = 0
        ans = [0 for x in range(num_people)]
        while True:
            if n == candies:
                return ans
            elif n > candies:
                a = candies - n + a
                if ln >= num_people:
                    ans[ln % num_people] += a
                else:
                    ans[ln] += a
                return ans
            else:
                a += 1
                n += a
                if n > candies:
                    a = candies - n + a
                    n = candies
                if ln >= num_people:
                    ans[ln % num_people] += a
                else:
                    ans[ln] += a
                ln += 1

    def distributeCandies2(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        i = 0
        while candies != 0:
            ans[i % num_people] += min(i + 1, candies)
            candies -= min(i + 1, candies)
            i += 1
        return ans

s = Solution()
print(s.distributeCandies(7, 4))
print(s.distributeCandies(10, 3))
print(s.distributeCandies(0, 3))
print(s.distributeCandies(1, 3))
print(s.distributeCandies(1, 3))

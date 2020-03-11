class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        执行用时 :120 ms, 在所有 Python 提交中击败了39.29%的用户
        内存消耗 :13 MB, 在所有 Python 提交中击败了100.00%的用户
        """
        from math import floor, sqrt
        rt = []
        for i in range(1, int(floor(target / 2)) + 1):
            n = (1 - 2 * i + sqrt((2 * i - 1) ** 2 + target * 8)) / 2
            if n % 1 == 0:
                rt.append([i + x for x in range(int(n))])
        return rt

    def findContinuousSequence2(self, target):
        """
        执行用时 :28 ms, 在所有 Python 提交中击败了92.86%的用户内存消耗 :14.5 MB, 在所有 Python 提交中击败了100.00%的用户
        执行用时 :28 ms, 在所有 Python 提交中击败了92.86%的用户内存消耗 :14.5 MB, 在所有 Python 提交中击败了100.00%的用户
        """
        res = []
        for n in range(2, target+1):
            temp = target - n*(n-1)//2  # temp = n*a_1
            if temp <= 0:
                break
            if not temp % n:
                a_1 = temp // n
                res.append([a_1 + i for i in range(n)])
        return res[::-1]


s= Solution()
print(s.findContinuousSequence2(15))

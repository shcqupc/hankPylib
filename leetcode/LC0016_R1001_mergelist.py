'''
面试题 10.01. 合并排序的数组 难度 简单
给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。
初始化 A 和 B 的元素数量分别为 m 和 n。
示例:
输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]
'''


class Solution(object):
    def merge1(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """
        A[m:] = B
        return A.sort()

    def merge2(self, A, m, B, n):
        pa, pb, tail = m - 1, n - 1, m + n - 1
        while pa >= 0 or pb >= 0:
            if pa == -1:
                A[tail] = B[pb]
                pb -= 1
            elif pb == -1:
                A[tail] = A[pa]
                pa -= 1
            elif A[pa] > B[pb]:
                A[tail] = A[pa]
                pa -= 1
            elif A[pa] <= B[pb]:
                A[tail] = B[pb]
                pb -= 1
            tail -= 1


s = Solution()
A = [4, 5, 6, 0, 0, 0]
B = [1, 2, 3]
s.merge2(A, 3, B, 3)
print(A)

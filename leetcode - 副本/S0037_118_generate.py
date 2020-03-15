class Solution(object):
    #####################################################
    # 杨辉三角I
    #####################################################
    def generate_1(self, numRows):
        """
        Dynamic programming
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows or numRows == -1:
            return []
        rslt = self.generate(numRows - 1)
        line = []
        for j in range(numRows):
            if j == 0 or j == numRows - 1:
                line.append(1)
            else:
                line.append(rslt[numRows - 2][j - 1] + rslt[numRows - 2][j])
        rslt.append(line)
        return rslt

    def generate_2(self, numRows):
        '''
        二项式
        :param numRows:
        :return:
        '''

        def com(n, m):
            n_1 = 1
            m_1 = 1
            n_m_1 = 1
            for i in range(1, n + 1):
                n_1 = n_1 * i
            for i in range(1, m + 1):
                m_1 = m_1 * i
            for i in range(1, n - m + 1):
                n_m_1 = n_m_1 * i
            return int(n_1 / m_1 / n_m_1)

        return [[com(i, j) for j in range(i + 1)] for i in range(numRows)]

    def generate_3(self, numRows):
        '''
        二项式
        :param numRows:
        :return:
        '''
        if not numRows or numRows == -1:
            return []
        rslt = [[j for j in range(i + 1)] for i in range(numRows)]
        for i in range(len(rslt)):
            for j in range(len(rslt[i])):
                if j == 0 or j == i:
                    rslt[i][j] = 1
                else:
                    rslt[i][j] = rslt[i - 1][j - 1] + rslt[i - 1][j]
        return rslt

    #####################################################
    # 杨辉三角II
    # 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
    #####################################################
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        def com(n, m):
            n_1 = 1
            m_1 = 1
            n_m_1 = 1
            for i in range(1, n + 1):
                n_1 = n_1 * i
            for i in range(1, m + 1):
                m_1 = m_1 * i
            for i in range(1, n - m + 1):
                n_m_1 = n_m_1 * i
            return int(n_1 / m_1 / n_m_1)

        return [com(rowIndex, j) for j in range(rowIndex + 1)]

    # 其实就是把杨辉三角1的空间复杂度进行优化的过程，理解了怎么优化，其实大部分DP问题里面的o(n^2)空间复杂度怎么优化成o(n)就会了
    def getRow_2(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [0] * (rowIndex + 1)
        res[0] = 1
        for i in range(rowIndex + 1):
            res[i] = 1
            for j in range(i - 1, 0, -1):
                res[j] += res[j - 1]
        return res


s = Solution()
# print(s.generate_3(None))
# print(s.generate_3(0))
# print(s.generate_3(1))
# print(s.generate_3(5))
print(s.getRow(3))

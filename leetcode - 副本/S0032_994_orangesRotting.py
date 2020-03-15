'''
    994. 腐烂的橘子难度简单148在给定的网格中，每个单元格可以有以下三个值之一：
	值 0 代表空单元格；
	值 1 代表新鲜橘子；
	值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。
'''


class Solution(object):
    def orangesRotting_1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import collections
        R, C = len(grid), len(grid[0])

        # queue - all starting cells with rotting oranges
        queue = collections.deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))

        def neighbors(r, c):
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d + 1))

        if any(1 in row for row in grid):
            return -1
        return d

    # 广度优先-集合的方式实现
    # 执行用时 :44 ms, 在所有 Python 提交中击败了55.56%的用户
    # 内存消耗 :11.9 MB, 在所有 Python 提交中击败了8.00%的用户
    def orangesRotting_2(self, grid):
        row = len(grid)
        col = len(grid[0])
        rotten = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}  # 腐烂集合
        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}  # 新鲜集合
        time = 0
        print(rotten, fresh, sep="    ")
        while fresh:
            if not rotten:
                return -1
            # 即将腐烂的如果在新鲜的集合中，就将它腐烂
            #####################################################
            '''drotten = set()
            for i, j in rotten:
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if (i + di, j + dj) in fresh:
                        drotten.add((i + di, j + dj))
            rotten = drotten'''
            #####################################################
            # 等价于↓
            rotten = {(i + di, j + dj) for i, j in rotten for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)] if
                      (i + di, j + dj) in fresh}
            fresh -= rotten  # 剔除腐烂的
            time += 1
        return time

    # 广度优先-队列的方式实现
    # 执行用时 :36 ms, 在所有 Python 提交中击败了88.14%的用户
    # 内存消耗 :11.7 MB, 在所有 Python 提交中击败了72.00%的用户
    def orangesRotting_3(self, grid):
        row, col, time = len(grid), len(grid[0]), 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = []
        # add the rotten orange to the queue
        # for i in range(row):
        #     for j in range(col):
        #         if grid[i][j] == 2:
        #             queue.append((i, j, time))
        queue = [(i, j, time) for i in range(row) for j in range(col) if grid[i][j] == 2]

        # bfs
        while queue:
            i, j, time = queue.pop(0)  # 弹个腐烂橘子出来
            for di, dj in directions:
                # 搜索当前腐烂的橘子能够腐烂的其它橘子
                if 0 <= i + di < row and 0 <= j + dj < col and grid[i + di][j + dj] == 1:
                    grid[i + di][j + dj] = 2  # 腐烂
                    queue.append((i + di, j + dj, time + 1))  # 腐烂橘子入队列

        # if there are still fresh oranges, return -1
        for row in grid:
            if 1 in row:
                return -1
        return time


s = Solution()
print(s.orangesRotting_3([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))

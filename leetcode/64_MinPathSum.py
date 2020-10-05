class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])

        costs = [[0] * w for i in range(h)]

        def inside(x, y):
            return -1 < x and -1 < y

        def cost(i, j):
            if inside(i-1, j) and inside(i, j-1):
                # print(costs[i-1][j], '+', costs[i][j-1], '+', grid[i][j])
                return min(costs[i-1][j], costs[i][j-1]) + grid[i][j]
            if inside(i-1, j):
                return costs[i-1][j] + grid[i][j]
            if inside(i, j-1):
                return costs[i][j-1] + grid[i][j]
            return grid[i][j]

        for i in range(h):
            for j in range(w):
                costs[i][j] = cost(i, j)
                
        # for i in range(h):
        #     print(costs[i])

        return costs[h-1][w-1]  
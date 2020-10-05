class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        paths = [[0] * w for i in range(h)]

        for i in range(h):
            if grid[i][0] == 1:
                break
            else:
                paths[i][0] = 1

        for i in range(w):
            if grid[0][i] == 1:
                break
            else:
                paths[0][i] = 1

        for i in range(1, h):
            for j in range(1, w):
                if grid[i][j] == 1:
                    continue
                paths[i][j] = paths[i-1][j] + paths[i][j-1]

        for i in range(h):
            print(paths[i])

        return paths[-1][-1]
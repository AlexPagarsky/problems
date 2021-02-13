
class Solution:
    def shortestPathBinaryMatrix(self, grid):
        N = len(grid)
        if grid[0][0] or grid[N-1][N-1]:
            return -1
        queue = [(0, 0, 1)]
        grid[0][0] = 1

        for i, j, length in queue:
            if i == N - 1 and j == N - 1:
                return length
                
            for x, y in ((i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)):
                if 0 <= x < N and 0 <= y < N and not grid[x][y]:
                    grid[x][y] = 1
                    queue.append((x, y, length + 1))

        return -1
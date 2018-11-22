class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        count = 0
        island = ((i,j) for i in range(n) for j in range(m) if grid[i][j] == 1)
        for i,j in island:
            count += 4
            if i+1 < n and grid[i+1][j] == 1:
                count -= 2
            if j+1 < m and grid[i][j+1] == 1:
                count -= 2
        return count
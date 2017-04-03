class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter =  0
        for i in range(0, len(grid)):
            # max perimeter given n is n*2 + 2, where there are n-2 2 squares and 2 3 squares
            for j in range(0, len(grid[i])):
                if i == 0 and grid[i][j] == 1:
                    if j == 0 or grid[i][j-1] == 0:
                        perimeter += 4
                    else:
                        perimeter += 2
                elif i != 0 and grid[i][j] == 1:
                    if j == 0 or grid[i][j-1] != 1:
                        if grid[i-1][j] == 1: # cell on top
                            perimeter += 2
                        else: # no cell on top
                            perimeter += 4
                    else:
                        if grid[i][j-1] == 1: # cell to the left
                            if grid[i-1][j] != 1: # no cell above
                                perimeter += 2
        return perimeter

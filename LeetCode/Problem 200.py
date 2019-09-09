# LeetCode: Problem 200
# Jonathan Kosasih

#Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
#You may assume all four edges of the grid are all surrounded by water.
#
#Example 1:
#Input:
#11110
#11010
#11000
#00000
#Output: 1
#
#Example 2:
#Input:
#11000
#11000
#00100
#00011
#Output: 3
#------------------------------------------------------------------
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if(not grid):
            return 0
        islands = 0
        queue = []
        visited = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] == "1" and visited[i][j] == 0):
                    visited[i][j] = 1
                    self.BFS(grid, visited, queue, i, j)
                    while(queue):
                        x, y = queue.pop(0)
                        self.BFS(grid, visited, queue, x, y)
                    islands += 1
        return islands
        
    def BFS(self, grid, visited, queue, i, j):
        upperBound = 0
        lowerBound = len(grid)-1
        leftBound = 0
        rightBound = len(grid[0])-1
        if(i >= upperBound and i <= lowerBound and j >= leftBound and j <= rightBound):
            # check top
            if(i-1 >= upperBound and grid[i-1][j] == "1" and visited[i-1][j] == 0):
                visited[i-1][j] = 1
                queue.append((i-1, j))
            # check right
            if(j+1 <= rightBound and grid[i][j+1] == "1" and visited[i][j+1] == 0):
                visited[i][j+1] = 1
                queue.append((i,j+1))
            # check bottom
            if(i+1 <= lowerBound and grid[i+1][j] == "1" and visited[i+1][j] == 0):
                visited[i+1][j] = 1
                queue.append((i+1, j))
            # check left
            if(j-1 >= leftBound and grid[i][j-1] == "1" and visited[i][j-1] == 0):
                visited[i][j-1] = 1
                queue.append((i,j-1))
        
sol = Solution()
example = [["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]]
print(str(sol.numIslands(example)))
example = [["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]]
print(str(sol.numIslands(example)))
example = [["1"],["0"],["1"],["0"],["1"],["1"]]
print(str(sol.numIslands(example)))
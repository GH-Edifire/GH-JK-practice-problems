# LeetCode: Problem 62
# Jonathan Kosasih

#A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
#The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
#How many possible unique paths are there?
#
#Note: m and n will be at most 100.
#
#Example 1:
#Input: m = 3, n = 2
#Output: 3
#Explanation:
#From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
#1. Right -> Right -> Down
#2. Right -> Down -> Right
#3. Down -> Right -> Right
#
#Example 2:
#Input: m = 7, n = 3
#Output: 28
#------------------------------------------------------------------
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for col in range(m) ] for row in range(n)]
        
        # all first row has 1 way of getting there
        for index in range(len(dp[0])):
            dp[0][index] = 1
        
        # all first column as 1 way of getting there
        for index in range(len(dp)):
            dp[index][0] = 1
        
        # rest of the array, current paths = paths above + paths on the left
        for y in range(1,len(dp)):
            for x in range(1,len(dp[0])):
                dp[y][x] = dp[y-1][x] + dp[y][x-1]
        # return the last index
        return dp[-1][-1]
        
sol = Solution()
print(sol.uniquePaths(3,2))
print(sol.uniquePaths(7,3))
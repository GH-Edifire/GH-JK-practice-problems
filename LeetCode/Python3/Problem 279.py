# LeetCode: Problem 279
# Jonathan Kosasih

#Given a positive integer n, find the least number of perfect square numbers
#(for example, 1, 4, 9, 16, ...) which sum to n.

#Example 1:
#Input: n = 12
#Output: 3 
#Explanation: 12 = 4 + 4 + 4.
#
#Example 2:
#Input: n = 13
#Output: 2
#Explanation: 13 = 4 + 9.
#------------------------------------------------------------------
# seems similar to the coin problem, but we need to figure out the max square number
class Solution:
    # DP, works but Time Limit Exceeded for Python3 
    def numSquares(self, n: int) -> int:
        # go from 0 to n inclusive
        sqNums = self.squareNumbers(n)
        dp = [[0 for x in range(n + 1)] for y in range(len(sqNums))]
        # first row setup
        for j in range(len(dp[0])):
            dp[0][j] = j
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if(j % sqNums[i] == 0):
                    dp[i][j] = dp[i][j-sqNums[i]] + 1
                else:
                    if(j - sqNums[i] >= 0):
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1] + 1, dp[i][j-sqNums[i]] + 1)
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1] + 1)
        return dp[-1][-1]
    
    # using BFS
    def numSquaresAlt(self, n: int) -> int:
        sqNums = self.squareNumbers(n)
        level = 0
        currentLevel = set()
        currentLevel.add(0)
        while(True):
            nextLevel = set()
            for cur in currentLevel:
                for num in sqNums:
                    if(cur + num == n):
                        return level + 1
                    if(cur + num < n):
                        nextLevel.add(cur + num)
            currentLevel = nextLevel
            level += 1
                
    def squareNumbers(self, limit):
        sqNums = []
        i = 1
        while(i*i <= limit):
            sqNums.append(i*i)
            i += 1
        return sqNums
sol = Solution()
print(str(sol.numSquaresAlt(6000)))
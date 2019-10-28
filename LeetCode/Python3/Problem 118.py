# LeetCode: Problem 118
# Jonathan Kosasih

#Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
#Example:
#Input: 5
#Output:
#[
#     [1],
#    [1,1],
#   [1,2,1],
#  [1,3,3,1],
# [1,4,6,4,1]
#]
#------------------------------------------------------------------
class Solution(object):
    # initial solution
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if(not numRows):
            return []
        if(numRows == 1):
            return [[1]]
        ans = [[1], [1,1]]
        for i in range(2,numRows):
            ans.append([])
            ans[i] = [1 for _ in range(i+1)]
            for j in range(1,len(ans[i])-1):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        return ans
    
    # more optimized
    def generateAlt(self, numRows):
        pascal = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal
    
sol = Solution()
print(str(sol.generate(1)))
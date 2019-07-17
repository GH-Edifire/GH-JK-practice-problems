# LeetCode: Problem 73
# Jonathan Kosasih

#Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
#
#Example 1:
#Input: 
#[
#  [1,1,1],
#  [1,0,1],
#  [1,1,1]
#]
#Output: 
#[
#  [1,0,1],
#  [0,0,0],
#  [1,0,1]
#]
#
#Example 2:
#Input: 
#[
#  [0,1,2,0],
#  [3,4,5,2],
#  [1,3,1,5]
#]
#Output: 
#[
#  [0,0,0,0],
#  [0,4,5,0],
#  [0,3,1,0]
#]
#------------------------------------------------------------------
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        firstRowHasZero = not all(matrix[0])
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j] == 0):
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])-1,-1,-1):
                if(matrix[0][j] == 0 or matrix[i][0] == 0):
                    matrix[i][j] = 0
        
        if(firstRowHasZero):
            matrix[0] = [0]*len(matrix[0])
    
    def setZeroesAlt(self, matrix):
        if len(matrix) == 0:
            return 
        rows = len(matrix)
        columns = len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    for temp in range(rows):
                        if matrix[temp][j] != 0:
                            matrix[temp][j] = 'a'
                    for temp in range(columns):
                        if matrix[i][temp] != 0:
                            matrix[i][temp] = 'a'
        
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0
        
                
sol = Solution()
example = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
sol.setZeroes(example)
print(example)
example = [
    [1,1,1],
    [0,1,2]
    ]
sol.setZeroes(example)
print(example)
# LeetCode: Problem 54
# Jonathan Kosasih

#Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
#Example 1:
#Input:
#[
# [ 1, 2, 3 ],
# [ 4, 5, 6 ],
# [ 7, 8, 9 ]
#]
#Output: [1,2,3,6,9,8,7,4,5]
#
#Example 2:
#Input:
#[
#  [1, 2, 3, 4],
#  [5, 6, 7, 8],
#  [9,10,11,12]
#]
#Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#------------------------------------------------------------------
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if(not matrix or len(matrix) == 0):
            return []
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])
        numbers = len(matrix) * len(matrix[0])
        ans = []
        while(len(ans) < numbers):
            for index in range(left, right, 1):
                if(len(ans) >= numbers):
                    break
                ans.append(matrix[top][index])
            for index in range(top + 1, bottom, 1):
                if(len(ans) >= numbers):
                    break
                ans.append(matrix[index][right - 1])
            for index in range(right - 2, left-1, -1):
                if(len(ans) >= numbers):
                    break
                ans.append(matrix[bottom - 1][index])
            for index in range(bottom - 2, top, -1):
                if(len(ans) >= numbers):
                    break
                ans.append(matrix[index][left])
                
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return ans
        
sol = Solution()
example = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print(str(sol.spiralOrder(example)))
example = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
print(str(sol.spiralOrder(example)))

# LeetCode: Problem 378
# Jonathan Kosasih

#Given a n x n matrix where each of the rows and columns are sorted in ascending order,
#find the kth smallest element in the matrix.
#
#Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
#Example:
#matrix = [
#   [ 1,  5,  9],
#   [10, 11, 13],
#   [12, 13, 15]
#],
#k = 8,
#return 13.
#------------------------------------------------------------------
import heapq
class Solution:
    def kthSmallest(self, matrix, k):
        heap = []
        # heap, smallest at the top
        heapq.heapify(heap)
        for row in matrix:
            for num in row:
                heapq.heappush(heap,num)
        ans = 0
        while(k != 0):
            ans = heapq.heappop(heap)
            k -= 1
        return ans
        
sol = Solution()
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
print(str(sol.kthSmallest(matrix, k)))

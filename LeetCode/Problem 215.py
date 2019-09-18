# LeetCode: Problem 215
# Jonathan Kosasih

#Find the kth largest element in an unsorted array.
#Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
#Example 1:
#Input: [3,2,1,5,6,4] and k = 2
#Output: 5
#
#Example 2:
#Input: [3,2,3,1,2,4,5,5,6] and k = 4
#Output: 4
#------------------------------------------------------------------
import heapq
class Solution(object):
    # use heap data structure
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[k-1]
    
    # just sort it in descending order and find the len(nums) - k index
    def findKthLargestAlt(self, nums, k):
        nums.sort(reverse = True)
        return nums[k-1]
    
sol = Solution()
nums = [3,2,1,5,6,4]
k = 2
print(str(sol.findKthLargest(nums, k)))
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(str(sol.findKthLargest(nums, k)))
print("--------------------------------")
nums = [3,2,1,5,6,4]
k = 2
print(str(sol.findKthLargestAlt(nums, k)))
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(str(sol.findKthLargestAlt(nums, k)))
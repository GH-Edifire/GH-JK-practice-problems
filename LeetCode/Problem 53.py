# LeetCode: Problem 53
# Jonathan Kosasih

#Given an integer array nums,
#find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
#Example:
#Input: [-2,1,-3,4,-1,2,1,-5,4],
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.
#------------------------------------------------------------------
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(not nums or len(nums) <= 0):
            return 0
        currentSum = 0
        greatestSum = 0
        for entry in nums[1:]:
            currentSum = max(entry, currentSum + entry)
            greatestSum = max(greatestSum, currentSum)
        return greatestSum
            
        
sol = Solution()
example = [-2,1,-3,4,-1,2,1,-5,4]
print(str(sol.maxSubArray(example)))

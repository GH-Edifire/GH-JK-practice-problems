# LeetCode: Problem 152
# Jonathan Kosasih

#Given an integer array nums, find the contiguous subarray within an array (containing at least one number)
#which has the largest product.
#
#Example 1:
#Input: [2,3,-2,4]
#Output: 6
#Explanation: [2,3] has the largest product 6.
#
#Example 2:
#Input: [-2,0,-1]
#Output: 0
#Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#------------------------------------------------------------------
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(not nums or len(nums) <= 0):
            return 0
        big, small, ans = nums[0], nums[0], nums[0]
        for i in range(1,len(nums)):
            temp = big
            # compare biggest * new number, the new number by itself, smallest * new number
            compare = [temp*nums[i], nums[i], small*nums[i]]
            big = max(compare)
            small = min(compare)
            if(big > ans):
                ans = big
        return ans
    
sol = Solution()
example = [2,3,-2,4]
print(str(sol.maxProduct(example)))
example = [-2,0,-1]
print(str(sol.maxProduct(example)))
example = [-2,3,-4]
print(str(sol.maxProduct(example)))


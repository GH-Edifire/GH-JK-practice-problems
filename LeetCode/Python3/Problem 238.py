# LeetCode: Problem 238
# Jonathan Kosasih

#Given an array nums of n integers where n > 1,
#return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
#
#Example:
#Input:  [1,2,3,4]
#Output: [24,12,8,6]
#
#Note: Please solve it without division and in O(n).
#------------------------------------------------------------------
class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        leftOfi = [1] * length
        rightOfi = [1] * length
        output = [1] * length
        for i in range(1, length):
            leftOfi[i] = nums[i-1] * leftOfi[i-1]
        for i in range(length-2, -1, -1):
            rightOfi[i] = nums[i+1] * rightOfi[i+1]
        for i in range(length):
            output[i] = leftOfi[i] * rightOfi[i]
        return output
        
sol = Solution()
example = [1,2,3,4]
print(sol.productExceptSelf(example))
# LeetCode: Problem 283
# Jonathan Kosasih

#Given an array nums, write a function to move all 0's
#to the end of it while maintaining the relative order of the non-zero elements.
#
#Example:
#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]
#
#Note:
#You must do this in-place without making a copy of the array.
#Minimize the total number of operations.
#------------------------------------------------------------------
class Solution:
    # use 2 pointers
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNumber = 0
        for i in range(len(nums)):
            if(nums[i] != 0):
                nums[lastNumber] = nums[i]
                lastNumber += 1
        for i in range(lastNumber, len(nums)):
            nums[i] = 0
            
sol = Solution()
example = [0,1,0,3,12]
sol.moveZeroes(example)
print(example)
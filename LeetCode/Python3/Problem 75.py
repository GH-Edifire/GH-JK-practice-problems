# LeetCode: Problem 75
# Jonathan Kosasih

#Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent,
#with the colors in the order red, white and blue.
#
#Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
#Note: You are not suppose to use the library's sort function for this problem.
#
#Example:
#Input: [2,0,2,1,1,0]
#Output: [0,0,1,1,2,2]
#------------------------------------------------------------------
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        mid = 0
        right = len(nums)-1
        while(mid <= right):
            if(nums[mid] == 0):
                self.swap(nums,left,mid)
                left += 1
                mid += 1
            elif(nums[mid] == 2):
                self.swap(nums,mid,right)
                right -= 1
            else:
                mid += 1
                
    def swap(self, nums, index1, index2):
        temp = nums[index1]
        nums[index1] = nums[index2]
        nums[index2] = temp
                
        
                
sol = Solution()
example = [2,0,2,1,1,0]
sol.sortColors(example)
print(example)
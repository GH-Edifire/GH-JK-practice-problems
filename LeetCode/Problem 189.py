# LeetCode: Problem 189
# Jonathan Kosasih

#Given an array, rotate the array to the right by k steps, where k is non-negative.
#
#Example 1:
#Input: [1,2,3,4,5,6,7] and k = 3
#Output: [5,6,7,1,2,3,4]
#Explanation:
#rotate 1 steps to the right: [7,1,2,3,4,5,6]
#rotate 2 steps to the right: [6,7,1,2,3,4,5]
#rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
#Example 2:
#Input: [-1,-100,3,99] and k = 2
#Output: [3,99,-1,-100]
#Explanation: 
#rotate 1 steps to the right: [99,-1,-100,3]
#rotate 2 steps to the right: [3,99,-1,-100]
#------------------------------------------------------------------
class Solution(object):
    # initial solution, O(1) space, brute force, takes a long time
    def rotateInitial(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp = 0
        i = 0
        while(i < k):
            temp = nums[len(nums)-1]
            for j in range(len(nums)-1,0,-1):
                nums[j] = nums[j-1]
            nums[0] = temp
            i += 1

    # take advantage of list methods
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0,nums.pop())
            
    # Python specific slicing
    def rotatePython(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        # nums[:] == changes values of nums, does not create a new reference
        nums[:] = nums[length - k:] + nums[:length - k]
        
sol = Solution()
example = [1,2,3,4,5,6,7]
k = 3
sol.rotate(example, k)
print(example)
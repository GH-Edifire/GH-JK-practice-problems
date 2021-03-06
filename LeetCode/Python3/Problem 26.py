# LeetCode: Problem 26
# Jonathan Kosasih

#Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
#
#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
#Example 1:
#Given nums = [1,1,2],
#
#Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
#
#It doesn't matter what you leave beyond the returned length.
#
#Example 2:
#Given nums = [0,0,1,1,1,2,2,3,3,4],
#
#Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
#
#It doesn't matter what values are set beyond the returned length.
#------------------------------------------------------------------
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        previous = None
        index = 0
        while(index < len(nums)):
            if(previous == nums[index]):
                nums.remove(nums[index])
                index -= 1
            else:
                previous = nums[index]
            index += 1
        return len(nums)
    
    # even simpler and faster, since we don't care about the array but rather the length,
    # so just count different numbers of the sorted array
    def removeDuplicates(self, A):
        if(not A):
            return 0

        newTail = 0

        for i in range(1, len(A)):
            if A[i] != A[newTail]:
                newTail += 1
                A[newTail] = A[i]

        return newTail + 1
        
sol = Solution()
nums = [1,1,2]
print(str(sol.removeDuplicates(nums)))
print(nums)
print("--------------------")
nums = [0,0,1,1,1,2,2,3,3,4]
print(str(sol.removeDuplicates(nums)))
print(nums)
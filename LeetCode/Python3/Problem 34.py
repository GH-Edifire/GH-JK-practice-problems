# LeetCode: Problem 34
# Jonathan Kosasih

#Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
#Your algorithm's runtime complexity must be in the order of O(log n).
#
#If the target is not found in the array, return [-1, -1].
#
#Example 1:
#Input: nums = [5,7,7,8,8,10], target = 8
#Output: [3,4]
#
#Example 2:
#Input: nums = [5,7,7,8,8,10], target = 6
#Output: [-1,-1]
#------------------------------------------------------------------
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if(not nums):
            return [-1,-1]
        first = 0
        last = len(nums) - 1
        foundOne = float("inf")
        foundTwo = float("-inf")
        # search for first occurance
        while(first <= last):
            mid = (first+last) // 2
            if(target == nums[mid]):
                foundOne = min(foundOne,mid)
                last = mid - 1
            elif(target > nums[mid]):
                first = mid + 1
            else:
                last = mid - 1
                
        # reset variables, search for 2nd occurance
        first = 0
        last = len(nums) - 1
        while(first <= last):
            mid = (first+last) // 2
            if(target == nums[mid]):
                foundTwo = max(foundTwo, mid)
                first = mid + 1
            elif(target > nums[mid]):
                first = mid + 1
            else:
                last = mid - 1
        
        # final checks
        foundOne = foundOne if(foundOne!=float("inf")) else -1
        foundTwo = foundTwo if(foundTwo!=float("-inf")) else -1
        return [foundOne, foundTwo]
    
sol = Solution()
example = [5,7,7,8,8,10]
target = 8
print(str(sol.searchRange(example, target)))

example = [5,7,7,8,8,10]
target = 6
print(str(sol.searchRange(example, target)))

example = [4,5,6,7,0,1,2]
target = 4
print(str(sol.searchRange(example, target)))

example = []
target = 3
print(str(sol.searchRange(example, target)))
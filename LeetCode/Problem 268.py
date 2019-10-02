# LeetCode: Problem 68
# Jonathan Kosasih

#Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
#Example 1:
#Input: [3,0,1]
#Output: 2
#
#Example 2:
#Input: [9,6,4,2,3,5,7,0,1]
#Output: 8
#
#Note:
#Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
#------------------------------------------------------------------
class Solution:
    def missingNumber(self, nums) -> int:
        if(not nums):
            return 0
        record = sum(list(range(len(nums)+1)))
        for num in nums:
            record -= num
        return record
    
    def missingNumberAlt(self, nums) -> int:
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number
                
        
sol = Solution()
example = [3,0,1]
print(str(sol.missingNumber(example)))
example = [9,6,4,2,3,5,7,0,1]
print(str(sol.missingNumber(example)))
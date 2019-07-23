# LeetCode: Problem 1
# Jonathan Kosasih

#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#Example:

#Given nums = [2, 7, 11, 15], target = 9,
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].
#------------------------------------------------------------------
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        data = {}
        index = 0
        for num in nums:
            comp = target - nums[index]
            if(comp in data.keys()):
                return [data[comp], index]
            data[num] = index
            index += 1
        return 0
    
sol = Solution()
example = [3,2,4]
target = 6
print(sol.twoSum(example,target))
    
nums = [2, 7, 11, 15]
target = 22
check = Solution()
answer = check.twoSum(nums, target)
if(answer == 0):
    print("Could not find indices to sum for " + str(target))
else:
    print(str(answer))
# LeetCode: Problem 198
# Jonathan Kosasih

#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
#the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
#it will automatically contact the police if two adjacent houses were broken into on the same night.
#
#Given a list of non-negative integers representing the amount of money of each house,
#determine the maximum amount of money you can rob tonight without alerting the police.
#
#Example 1:
#Input: [1,2,3,1]
#Output: 4
#Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#             Total amount you can rob = 1 + 3 = 4.
#             
#Example 2:
#Input: [2,7,9,3,1]
#Output: 12
#Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#             Total amount you can rob = 2 + 9 + 1 = 12.
#------------------------------------------------------------------
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(not nums):
            return 0
        if(len(nums) <= 2):
            return max(nums)
        memo = [0] * len(nums)
        memo[0] = nums[0]
        memo[1] = max(nums[0],nums[1])
        for i in range(2, len(nums)):
            # track what's bigger: current + sum[i-2] or sum[i-1]
            memo[i] = max(nums[i] + memo[i-2], memo[i-1])
        return memo[-1]
    
    # For constant space, but slower
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(not nums):
            return 0
        if(len(nums) <= 2):
            return max(nums)
        prev = 0
        curr = 0
        for num in nums:
            temp = prev
            prev = curr
            curr = max(num + temp, prev)
        return curr
        
sol = Solution()
example = [1,2,3,1]
print(str(sol.rob(example)))
example = [2,7,9,3,1]
print(str(sol.rob(example)))
example = [1,2,3,1,6,7,1,5,6,4]
print(str(sol.rob(example)))
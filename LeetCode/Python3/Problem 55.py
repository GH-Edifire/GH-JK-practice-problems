# LeetCode: Problem 55
# Jonathan Kosasih

#Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
#Each element in the array represents your maximum jump length at that position.
#
#Determine if you are able to reach the last index.
#
#Example 1:
#Input: [2,3,1,1,4]
#Output: true
#Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#Example 2:
#Input: [3,2,1,0,4]
#Output: false
#Explanation: You will always arrive at index 3 no matter what. Its maximum
#             jump length is 0, which makes it impossible to reach the last index.
#------------------------------------------------------------------
class Solution(object):
    # faster version, but no DP
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxDistance = 0
        n = len(nums)
        for i, x in enumerate(nums):
            # if max distance is ever lower than current index, we can never make it to the end
            if(maxDistance < i):
                return False
            # we can reach the end
            if(maxDistance >= n - 1):
                return True
            # max distance = the bigger of maxDistance and the new jumpable value
            maxDistance = max(maxDistance, i + x)
    
    
    
    # works but too slow for leetcode
    # DP, build up from the beginning, flagging in memo if we can reach an index or not
    def canJumpInitial(self, nums):
        if(not nums):
            return False
        memo = [False] * len(nums)
        memo[0] = True
        for index in range(len(nums)):
            for jumpRange in range(1,nums[index]+1):
                if(memo[index] == False or jumpRange+index > len(nums)-1):
                    break
                memo[jumpRange+index] = True
                
        return memo[len(nums)-1]
        
sol = Solution()
example = [2,3,1,1,4]
print(str(sol.canJump(example)))
example = [3,2,1,0,4]
print(str(sol.canJump(example)))

example = [0,1,0,0,0,0,0,0,0,0,5,1]
print(str(sol.canJump(example)))
example = [2,0,0]
print(str(sol.canJump(example)))


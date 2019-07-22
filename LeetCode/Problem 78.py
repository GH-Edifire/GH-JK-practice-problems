# LeetCode: Problem 78
# Jonathan Kosasih

#Given a set of distinct integers, nums, return all possible subsets (the power set).
#
#Note: The solution set must not contain duplicate subsets.
#------------------------------------------------------------------
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for num in sorted(nums):
            ans += [item+[num] for item in ans]
        return ans
                
sol = Solution()
example = [1,2,3]
example = sol.subsets(example)
print(example)
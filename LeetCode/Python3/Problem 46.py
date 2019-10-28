# LeetCode: Problem 46
# Jonathan Kosasih

#Given a collection of distinct integers, return all possible permutations.

#Example:
#Input: [1,2,3]
#Output:
#[
#  [1,2,3],
#  [1,3,2],
#  [2,1,3],
#  [2,3,1],
#  [3,1,2],
#  [3,2,1]
#]
#------------------------------------------------------------------
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # permuting n numbers, take the nth number and add it to the n-1 number list in every possible position
        perms = [[]]   
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm)+1):   
                    new_perms.append(perm[:i] + [n] + perm[i:])
            perms = new_perms
        return perms
        

sol = Solution()
print(sol.permute([1,2,3]))
print("//--------")
print(sol.permute([1,2,3,4]))
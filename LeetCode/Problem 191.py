# LeetCode: Problem 191
# Jonathan Kosasih

# Write a function that takes an unsigned integer and return the number of '1' bits it has
#------------------------------------------------------------------
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        value = n
        while(value > 0):
            ans += value & 0x1
            value = value >> 1
        return ans
        
sol = Solution()
example = 11
print(str(sol.hammingWeight(example)))
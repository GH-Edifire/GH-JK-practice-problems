# LeetCode: Problem 172
# Jonathan Kosasih

#Given an integer n, return the number of trailing zeroes in n!.
#------------------------------------------------------------------
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while(n > 0):
            n = n // 5
            ans += n
        return ans
        
sol = Solution()
example = 25
print(str(sol.trailingZeroes(example)))
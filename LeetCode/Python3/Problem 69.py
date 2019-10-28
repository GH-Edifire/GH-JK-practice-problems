# LeetCode: Problem 69
# Jonathan Kosasih

#Implement int sqrt(int x).
#
#Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#
#Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
#
#Example 1:
#Input: 4
#Output: 2
#
#Example 2:
#Input: 8
#Output: 2
#Explanation: The square root of 8 is 2.82842..., and since 
#             the decimal part is truncated, 2 is returned.
#------------------------------------------------------------------
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Newton's method
        ans = x
        while (ans*ans > x):
            ans = (ans + x//ans) // 2
        return ans
        
                
sol = Solution()
example = 4
print(sol.mySqrt(example))
example = 8
print(sol.mySqrt(example))
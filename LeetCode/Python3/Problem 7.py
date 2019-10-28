# LeetCode: Problem 7
# Jonathan Kosasih

# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:
# Input: 123
# Output: 321

# Example 2:
# Input: -123
# Output: -321

# Example 3:
# Input: 120
# Output: 21

# Note:
# Assume we are dealing with an environment which could only store integers within the
# 32-bit signed integer range: [−2^31 to 2^31 − 1]. For the purpose of this problem,
# assume that your function returns 0 when the reversed integer overflows.
#------------------------------------------------------------------
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = x < 0
        answer = str(abs(x))
        answer = answer[::-1]
        if(neg):
            answer = "-" + answer
        answer = int(answer)
        if (answer < -(2**31) or answer > (2**31 - 1)):
            return 0
        return answer

# Tests
sol = Solution()
example1 = 123
example2 = -123
example3 = 120
example4 = -2**31
test = sol.reverse(example1)
print(test)
test = sol.reverse(example2)
print(test)
test = sol.reverse(example3)
print(test)
test = sol.reverse(example4)
print(test)

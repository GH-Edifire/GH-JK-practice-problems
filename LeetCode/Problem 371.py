# LeetCode: Problem 371
# Jonathan Kosasih

#Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
#
#Example 1:
#Input: a = 1, b = 2
#Output: 3
#
#Example 2:
#Input: a = -2, b = 3
#Output: 1
#------------------------------------------------------------------
# Python has "unlimited bits" for numbers as it scales depending on what is stored. We need to make a range for it.
# Python also stores numbers in 2's complement, but when you "&" it, it unsigns the number and can get a massive integer.
# if "a" was negative and gets unsigned, results in a huge number. Just convert it back to signed

#https://leetcode.com/problems/sum-of-two-integers/discuss/84282/Python-solution-with-no-%22%2B-*%22-completely-bit-manipulation-guaranteed
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)
    
#https://leetcode.com/problems/sum-of-two-integers/discuss/84350/Most-Straightforward-Python-Solution!
    def getSumAlt(self, a: int, b: int) -> int:
        if a == 0:
            return b
        elif b == 0:
            return a
        
        mask = 0xffffffff
 
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        # a is negative if the first bit is 1
        if (a >> 31) & 1:
            return ~(a ^ mask)
        else:
            return a
        
sol = Solution()
a = 1
b = 2
print(str(sol.getSum(a,b)))
a = -2
b = 3
print(str(sol.getSum(a,b)))
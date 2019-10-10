# LeetCode: Problem 326
# Jonathan Kosasih

#Given an integer, write a function to determine if it is a power of three.
#------------------------------------------------------------------
class Solution:
    # first way, just divide
    def isPowerOfThree(self, n: int) -> bool:
        if(n < 1):
            return False
        while(n % 3 == 0):
            n /= 3
        return n == 1
    
    # second way
    # max int is 2147483647 for 4 byte integer
    def isPowerOfThreeAlt(self, n: int) -> bool:
        # 3^log3 maxInt == 3^19.56 == 3^19 == 1162261467
        # 3^1 -> 3^19 will divide successfully into 1162261467, just check that number
        return n > 0 and 1162261467 % n == 0

sol = Solution()
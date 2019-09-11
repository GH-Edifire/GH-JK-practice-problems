# LeetCode: Problem 202
# Jonathan Kosasih

#Write an algorithm to determine if a number is "happy".
#
#A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
#
#Example: 
#Input: 19
#Output: true
#Explanation: 
#12 + 92 = 82
#82 + 22 = 68
#62 + 82 = 100
#12 + 02 + 02 = 1
#------------------------------------------------------------------
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(not n):
            return False
        # could also build this empty in the while loop
        memo = {"0": 0,"1": 1, "2": 4, "3": 9, "4": 16, "5": 25, "6": 36, "7": 49, "8": 64,"9": 81}
        seen = set()
        string = str(n)
        sum = 0
        while(string != "1"):
            if(string in seen):
                return False
            else:
                seen.add(string)
            for char in string:
                sum += memo[char]
            string = str(sum)
            sum = 0
        return True
        
        
sol = Solution()
example = 22
print(str(sol.isHappy(example)))
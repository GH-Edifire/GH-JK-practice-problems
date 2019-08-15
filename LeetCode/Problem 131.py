# LeetCode: Problem 131
# Jonathan Kosasih

#Given a string s, partition s such that every substring of the partition is a palindrome.
#
#Return all possible palindrome partitioning of s.
#
#Example:
#Input: "aab"
#Output:
#[
#  ["aa","b"],
#  ["a","a","b"]
#]
#------------------------------------------------------------------
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        memo = dict()
        return self.helper(s, memo)
    
    def helper(self, s, memo):
        if(s in memo):
            return memo[s]
        elif(not s):
            memo[s] = [[]]
        else:
            temp = []
            for i in range(1, len(s)+1):
                if(self.palindrome(s[:i])):
                    for partition in self.helper(s[i:], memo):
                        temp.append([s[:i]] + partition)
            memo[s] = temp
        return memo[s]
        
    def palindrome(self, s):
        return "".join(reversed(s)) == s
        
        
sol = Solution()
string = "aab"
print(str(sol.partition(string)))

# LeetCode: Problem 387
# Jonathan Kosasih

#Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
#Examples:
#s = "leetcode"
#return 0.
#
#s = "loveleetcode",
#return 2.
#------------------------------------------------------------------
class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = 0
        memo = dict()
        for char in s:
            if(char not in memo):
                memo[char] = index
            else:
                flag = False
                memo[char] = -2
            index += 1
        for key in memo:
            if(memo[key] >= 0):
                return memo[key]
        return -1
               
sol = Solution()
s = "leetcode"
print(str(sol.firstUniqChar(s)))
s = "loveleetcode"
print(str(sol.firstUniqChar(s)))
s = "abcd"
print(str(sol.firstUniqChar(s)))
s = "a"
print(str(sol.firstUniqChar(s)))
s = "aa"
print(str(sol.firstUniqChar(s)))
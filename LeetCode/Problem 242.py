# LeetCode: Problem 242
# Jonathan Kosasih

#Given two strings s and t , write a function to determine if t is an anagram of s.
#
#Example 1:
#Input: s = "anagram", t = "nagaram"
#Output: true
#
#Example 2:
#Input: s = "rat", t = "car"
#Output: false
#------------------------------------------------------------------
class Solution:
    # sort both strings then compare
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    # use hashtable and make sure there are the same amount of chars in each
    def isAnagramAlt(self, s: str, t: str) -> bool:
        memo = dict()
        for char in s:
            if(char not in memo):
                memo[char] = 1
            else:
                memo[char] += 1
        for char in t:
            if(char not in memo):
                memo[char] = 1
            else:
                memo[char] -= 1
        for char in memo:
            if(memo[char] != 0):
                return False
        return True
                
        
sol = Solution()
s = "anagram"
t = "nagaram"
print(sol.isAnagram(s, t))
s = "rat"
t = "car"
print(sol.isAnagram(s, t))
print("-------------------------")
s = "anagram"
t = "nagaram"
print(sol.isAnagramAlt(s, t))
s = "rat"
t = "car"
print(sol.isAnagramAlt(s, t))
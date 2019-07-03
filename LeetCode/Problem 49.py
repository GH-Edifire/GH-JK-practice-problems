# LeetCode: Problem 49
# Jonathan Kosasih

#Given an array of strings, group anagrams together.
#
#Example:
#
#Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
#Output:
#[
#  ["ate","eat","tea"],
#  ["nat","tan"],
#  ["bat"]
#]
#Note:
#
#All inputs will be in lowercase.
#The order of your output does not matter.
#------------------------------------------------------------------
import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = collections.defaultdict(list)
        for string in strs:
            # sort the string for the dictionary, all anagrams will have the same sorted key
            # append unchanged string to sorted key
            ans[tuple(sorted(string))].append(string)
        return ans.values()
        
sol = Solution()
example1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
example1 = sol.groupAnagrams(example1)
for values in example1:
    print(values)
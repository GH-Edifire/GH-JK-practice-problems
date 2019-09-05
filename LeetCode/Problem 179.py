# LeetCode: Problem 179
# Jonathan Kosasih

#Given a list of non negative integers, arrange them such that they form the largest number.
#
#Example 1:
#Input: [10,2]
#Output: "210"
#
#Example 2:
#Input: [3,30,34,5,9]
#Output: "9534330"
#Note: The result may be very large, so you need to return a string instead of an integer.
#------------------------------------------------------------------
# STUDY SOLUTION!
# algorithm:
# convert nums to str entries
# sort entries using custom comparator (x+y > y+x)
# join strings, if 0 is first entry just return 0 (case of all 0s inputted)
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
        
        
sol = Solution()
example = [10,2]
print(str(sol.largestNumber(example)))
example = [3,30,34,5,9]
print(str(sol.largestNumber(example)))
example = [1,2,3,4,5]
print(str(sol.largestNumber(example)))
# LeetCode: Problem 169
# Jonathan Kosasih

#Given an array of size n, find the majority element.
#The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
#You may assume that the array is non-empty and the majority element always exist in the array.
#------------------------------------------------------------------
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        record = dict()
        for num in nums:
            if(str(num) not in record):
                record[str(num)] = 1
            else:
                record[str(num)] += 1
        return max(record, key=record.get)
        
sol = Solution()
example = [3,2,3]
print(str(sol.majorityElement(example)))
example = [2,2,1,1,1,2,2]
print(str(sol.majorityElement(example)))

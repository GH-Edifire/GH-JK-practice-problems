# LeetCode: Problem 136
# Jonathan Kosasih

#Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
#Note:
#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
#Example 1:
#Input: [2,2,1]
#Output: 1
#
#Example 2:
#Input: [4,1,2,1,2]
#Output: 4
#------------------------------------------------------------------
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(not nums):
            return 0
        hashTable = dict()
        for num in nums:
            if(num not in hashTable):
                hashTable[num] = 1
            else:
                hashTable[num] += 1
        return min(hashTable, key = lambda x: hashTable.get(x))
    
    def singleNumberXOR(self,nums):
        ans = 0
        for num in nums:
            ans ^= num
        return ans
sol = Solution()
example = [2,2,1]
print(str(sol.singleNumber(example)))
example = [4,1,2,1,2]
print(str(sol.singleNumberXOR(example)))
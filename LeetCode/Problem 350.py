# LeetCode: Problem 350
# Jonathan Kosasih

#Given two arrays, write a function to compute their intersection.
#
#Example 1:
#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2,2]
#
#Example 2:
#Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#Output: [4,9]
#
#Note:
#Each element in the result should appear as many times as it shows in both arrays.
#The result can be in any order.
#------------------------------------------------------------------
class Solution:
    def intersect(self, nums1, nums2):
        output = []
        d = dict()
        for num in nums1:
            if(num not in d):
                d[num] = 1
            else:
                d[num] += 1
        for num in nums2:
            if(num in d and d[num] > 0):
                output.append(num)
                d[num] -= 1
        return output
        
sol = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(str(sol.intersect(nums1,nums2)))
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(str(sol.intersect(nums1,nums2)))
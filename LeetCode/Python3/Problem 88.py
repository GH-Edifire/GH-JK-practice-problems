# LeetCode: Problem 88
# Jonathan Kosasih

#Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
#Note:
#The number of elements initialized in nums1 and nums2 are m and n respectively.
#You may assume that nums1 has enough space (size that is greater or equal to m + n)
#to hold additional elements from nums2.
#
#Example:
#Input:
#nums1 = [1,2,3,0,0,0], m = 3
#nums2 = [2,5,6],       n = 3
#
#Output: [1,2,2,3,5,6]
#------------------------------------------------------------------
class Solution(object):
    # swap with 2nd array, add 2nd array to 1st at the end
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if(nums1 is None or nums2 is None):
            return
        if(n == 0):
            return
        
        i = 0
        j = 0
        limit = m+n
        while(i < limit):
            if(nums1[i] <= nums2[j] and i < m):
                i += 1
            elif(nums1[i] > nums2[j] and i < m):
                temp = nums2[j]
                nums2[j] = nums1[i]
                nums1[i] = temp
                i += 1
                # resort 2nd array just in case
                nums2.sort()
            else:
                nums1[i] = nums2[j]
                i += 1
                j += 1
    
    # faster, fill from the end to start
    def mergeAlt(self, nums1, m, nums2, n):
        index1 = m-1
        index2 = n-1
        current = m + n - 1
        while(index1 >= 0 and index2 >= 0):
            if(nums1[index1] > nums2[index2]):
                nums1[current] = nums1[index1]
                index1 -= 1
            else:
                nums1[current] = nums2[index2]
                index2 -= 1
            current -= 1
        if(index2 >= 0):
            for i in range(index2 + 1):
                nums1[i] = nums2[i]
        
        
sol = Solution()
example = [1,2,3,0,0,0]
m = 3
example2 = [2,5,6]
n = 3
#example = [4,5,6,0,0,0]
#m = 3
#example2 = [1,2,3]
#n = 3
sol.mergeAlt(example, m, example2, n)
print(example)
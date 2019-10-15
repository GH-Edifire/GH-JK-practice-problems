# LeetCode: Problem 334
# Jonathan Kosasih

#Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
#
#Formally the function should:
#Return true if there exists i, j, k
#such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
#
#Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.
#------------------------------------------------------------------
class Solution:
    def increasingTriplet(self, nums):
        first = second = float("inf")
        for num in nums:
            if(num <= first):
                first = num
            elif(num <= second):
                second = num
            else:
                return True
        return False
    
sol = Solution()
nums = [1,2,3,4,5]
print(sol.increasingTriplet(nums))
nums = [5,4,3,2,1]
print(sol.increasingTriplet(nums))

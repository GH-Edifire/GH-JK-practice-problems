# LeetCode: Problem 384
# Jonathan Kosasih

#Shuffle a set of numbers without duplicates.
#
#Example:
#// Init an array with set 1, 2, and 3.
#int[] nums = {1,2,3};
#Solution solution = new Solution(nums);
#
#// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
#solution.shuffle();
#
#// Resets the array back to its original configuration [1,2,3].
#solution.reset();
#
#// Returns the random shuffling of array [1,2,3].
#solution.shuffle();
#------------------------------------------------------------------
import random
class Solution:

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        ans = self.nums[:]
        for i in range(len(ans)-1, 0, -1):
            j = random.randrange(0, i+1)
            ans[i], ans[j] = ans[j], ans[i]
        return ans
               
sol = Solution([1,2,3])
print(sol.shuffle())
print(sol.reset())

# LeetCode: Problem 1
# Jonathan Kosasih

#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#Example:

#Given nums = [2, 7, 11, 15], target = 9,
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].
#------------------------------------------------------------------
class Solution(object):
    def twoSum(self, nums, target):
        index = 0
        data = {}
        # place list into dictionary
        for i in nums:
            data[index] = nums[index]
            #print("data["+str(index)+"] = " + str(data.get(index)))
            index = index + 1
        # check if complement is in dictionary
        for i in data:
            check = target - data[i]
            if(check in data.values()):
                # found complementary values in dictionary
                x = -1
                y = -1
                # return the first instances of complementary values
                for j in data:
                    if(data[j] == data[i]):
                        x = j
                    elif(data[j] == check):
                        y = j
                # build return indices
                answer = [x, y]
                return answer
        # no complementary values
        return 0
    
nums = [2, 7, 11, 15]
target = 22
check = Solution()
answer = check.twoSum(nums, target)
if(answer == 0):
    print("Could not find indices to sum for " + str(target))
else:
    print(str(answer))
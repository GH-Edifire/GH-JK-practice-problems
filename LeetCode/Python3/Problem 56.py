# LeetCode: Problem 56
# Jonathan Kosasih

#Given a collection of intervals, merge all overlapping intervals.
#
#Example 1:
#Input: [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#
#Example 2:
#Input: [[1,4],[4,5]]
#Output: [[1,5]]
#Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#------------------------------------------------------------------
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if(not intervals):
            return []
        intervals = sorted(intervals, key=lambda entry: entry[0])
        ans = [intervals[0]]
        for index in range(1,len(intervals)):
            if(ans[-1][-1] >= intervals[index][0]):
                ans[-1][-1] = max(ans[-1][-1], intervals[index][1])
            else:
                ans.append(intervals[index])
        return ans
        
sol = Solution()
example = [[1,3],[2,6],[8,10],[15,18]]
print(sol.merge(example))
example = [[1,4],[4,5]]
print(sol.merge(example))
example = [[1,4],[0,4]]
print(sol.merge(example))
example = [[1,4],[0,1]]
print(sol.merge(example))
example = [[1,4],[0,0]]
print(sol.merge(example))
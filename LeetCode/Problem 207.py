# LeetCode: Problem 207
# Jonathan Kosasih

#There are a total of n courses you have to take, labeled from 0 to n-1.
#
#Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
#which is expressed as a pair: [0,1]
#
#Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
#Example 1:
#Input: 2, [[1,0]] 
#Output: true
#Explanation: There are a total of 2 courses to take. 
#             To take course 1 you should have finished course 0. So it is possible.
#             
#Example 2:
#Input: 2, [[1,0],[0,1]]
#Output: false
#Explanation: There are a total of 2 courses to take. 
#             To take course 1 you should have finished course 0, and to take course 0 you should
#             also have finished course 1. So it is impossible.
#------------------------------------------------------------------
import collections
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(set)
        neighbors = collections.defaultdict(set)
        for course, pre in prerequisites:
            graph[course].add(pre)
            neighbors[pre].add(course)
        queue = [i for i in range(numCourses) if not graph[i]]
        count = 0
        while(queue):
            node = queue.pop()
            count += 1
            for neighbor in neighbors[node]:
                graph[neighbor].remove(node)
                if(not graph[neighbor]):
                    queue.append(neighbor)
        return count == numCourses

sol = Solution()
print(str(sol.canFinish(2, [[1,0]]))) # true
print(str(sol.canFinish(2, [[1,0],[0,1]]))) # false
print(str(sol.canFinish(4, [[2,1], [1,0]]))) # true
print(str(sol.canFinish(3, [[1,0],[1,2],[0,1]]))) # false
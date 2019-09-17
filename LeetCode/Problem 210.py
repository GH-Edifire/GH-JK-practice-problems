# LeetCode: Problem 210
# Jonathan Kosasih

#There are a total of n courses you have to take, labeled from 0 to n-1.
#
#Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
#which is expressed as a pair: [0,1]
#
#Given the total number of courses and a list of prerequisite pairs,
#return the ordering of courses you should take to finish all courses.
#
#There may be multiple correct orders, you just need to return one of them.
#If it is impossible to finish all courses, return an empty array.
#
#Example 1:
#Input: 2, [[1,0]] 
#Output: [0,1]
#Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
#             course 0. So the correct course order is [0,1] .
#Example 2:
#Input: 4, [[1,0],[2,0],[3,1],[3,2]]
#Output: [0,1,2,3] or [0,2,1,3]
#Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
#             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
#             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
#------------------------------------------------------------------
# almost the same as LC 207, just modify it to record classes with a stack/queue
import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
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
        courses = []
        queue = [i for i in range(numCourses) if not graph[i]]
        while(queue):
            node = queue.pop()
            courses.append(node)
            for neighbor in neighbors[node]:
                graph[neighbor].remove(node)
                if(not graph[neighbor]):
                    queue.append(neighbor)
        return courses if len(courses) == numCourses else []

sol = Solution()
print(str(sol.findOrder(2, [[1,0]]))) # true
print(str(sol.findOrder(2, [[1,0],[0,1]]))) # false
print(str(sol.findOrder(4, [[2,1], [1,0]]))) # true
print(str(sol.findOrder(3, [[1,0],[1,2],[0,1]]))) # false
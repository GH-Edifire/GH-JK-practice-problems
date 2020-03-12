// LeetCode: Problem 210
// Jonathan Kosasih
/*
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
*/
//-------------------------------------------------------------------

#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <string>
#include <algorithm> 
#include <stack>
#include <queue>
#include <deque>
#include <numeric>
using std::vector;
using std::map;
using std::unordered_map;
using std::set;
using std::stack;
using std::queue;
using std::deque;
using std::accumulate;

// STUDY TOPOLOGICAL SORT
class Solution {
public:
	vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
		vector<int> res;
		vector<vector<int>> graph(numCourses + 3);
		vector<int> indegree(numCourses + 3, 0);
		for (auto item : prerequisites) {
			graph[item[1]].push_back(item[0]);
			++indegree[item[0]];
		}
		for (int i = 0; i < numCourses; ++i) {
			int tmp = 0;
			while (indegree[tmp] != 0 && tmp < numCourses) ++tmp;
			if (tmp == numCourses) break;
			indegree[tmp] = -1;
			res.push_back(tmp);
			for (int j = 0; j < graph[tmp].size(); ++j) {
				--indegree[graph[tmp][j]];
			}
		}
		if (res.size() < numCourses) return {};
		return res;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
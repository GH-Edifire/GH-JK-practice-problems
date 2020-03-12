// LeetCode: Problem 207
// Jonathan Kosasih
/*
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
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

class Solution {
public:
	// STUDY TOPOLOGICAL SORT
	bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {

		vector<unordered_set<int>> matrix(numCourses); // save this directed graph
		for (int i = 0; i < prerequisites.size(); ++i)
			matrix[prerequisites[i][1]].insert(prerequisites[i][0]);

		vector<int> d(numCourses, 0); // in-degree
		for (int i = 0; i < numCourses; ++i)
			for (auto it = matrix[i].begin(); it != matrix[i].end(); ++it)
				++d[*it];

		for (int j = 0, i; j < numCourses; ++j)
		{
			for (i = 0; i < numCourses && d[i] != 0; ++i); // find a node whose in-degree is 0

			if (i == numCourses) // if not find
				return false;

			d[i] = -1;
			for (auto it = matrix[i].begin(); it != matrix[i].end(); ++it)
				--d[*it];
		}

		return true;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
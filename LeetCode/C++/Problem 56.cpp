// LeetCode: Problem 56
// Jonathan Kosasih
/*
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
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
using std::vector;
using std::map;
using std::unordered_map;
using std::set;

class Compare {
public:
	bool operator () (vector<int>& vec1, vector<int>& vec2) {
		return vec1[0] < vec2[0];
	}
};

Compare CompObject;

class Solution {
public:
	vector<vector<int>> merge(vector<vector<int>>& intervals) {
		if (intervals.empty())
			return {};

		sort(intervals.begin(), intervals.end(), CompObject);

		int i = 0;
		vector<vector<int>> res;
		while (i < intervals.size() - 1) {
			if (intervals[i][1] < intervals[i + 1][0])
				res.push_back(intervals[i]);

			else if (intervals[i][1] >= intervals[i + 1][0] && intervals[i][1] < intervals[i + 1][1])
				intervals[i + 1][0] = intervals[i][0];

			else {
				intervals[i + 1][0] = intervals[i][0];
				intervals[i + 1][1] = intervals[i][1];
			}
			i++;
		}

		res.push_back(intervals[i]);
		return res;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
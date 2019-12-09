// LeetCode: Problem 62
// Jonathan Kosasih
/*
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
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

class Solution {
public:
	int uniquePaths(int m, int n) {
		vector<vector<int>> dp(m, vector<int>(n, 0));
		// first row only has 1 way of getting there
		for (int i = 0; i < dp[0].size(); i++) {
			dp[0][i] = 1;
		}
		// first column only has 1 way of getting there
		for (int i = 0; i < dp.size(); i++) {
			dp[i][0] = 1;
		}
		// rest of array, current paths = paths above + paths on the left
		for (int i = 1; i < dp.size(); i++) {
			for (int j = 1; j < dp[0].size(); j++) {
				dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
			}
		}
		return dp[dp.size() - 1][dp[0].size() - 1];
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
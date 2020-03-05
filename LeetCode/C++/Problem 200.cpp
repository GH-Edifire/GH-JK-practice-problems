// LeetCode: Problem 200
// Jonathan Kosasih
/*
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
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
private:
	void dfs(vector<vector<char>>& grid, int i, int j, int m, int n) {
		if (i >= 0 && i < m && j >= 0 && j < n && grid[i][j] == '1') {
			grid[i][j] = '2'; // mark to avoid recounting
			dfs(grid, i + 1, j, m, n);
			dfs(grid, i - 1, j, m, n);
			dfs(grid, i, j + 1, m, n);
			dfs(grid, i, j - 1, m, n);
		}
	}
public:
	int numIslands(vector<vector<char>>& grid) {
		int m = (int)grid.size();
		if (m == 0) return 0;
		int n = (int)grid[0].size();
		if (n == 0) return 0;
		int res = 0;
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				if (grid[i][j] == '1') {
					res++;
					dfs(grid, i, j, m, n);
				}
			}
		}
		return res;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
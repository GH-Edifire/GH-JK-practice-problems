// LeetCode: Problem 118
// Jonathan Kosasih
/*
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
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
using std::vector;
using std::map;
using std::unordered_map;
using std::set;
using std::stack;
using std::queue;
using std::deque;

class Solution {
public:
	vector<vector<int>> generate(int numRows) {
		vector<vector<int>> answer(numRows);
		for (int i = 0; i < numRows; i++) {
			answer[i].resize(i + 1);
			answer[i][0] = answer[i][i] = 1; // fill out sides of triangle
			for (int j = 1; j < i; j++) {
				answer[i][j] = answer[i - 1][j - 1] + answer[i - 1][j];
			}
		}
		return answer;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
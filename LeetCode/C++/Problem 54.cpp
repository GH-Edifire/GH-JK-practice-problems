// LeetCode: Problem 54
// Jonathan Kosasih
/*
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
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
	vector<int> spiralOrder(vector<vector<int>>& matrix) {
		vector<int> answer;
		if (matrix.empty()) {
			return answer;
		}
		int top = 0;
		int bottom = matrix.size();
		int left = 0;
		int right = matrix[0].size();
		int totalSize = matrix.size() * matrix[0].size();
		while (answer.size() < totalSize) {
			for (int i = left; i < right; i++) {
				if (answer.size() >= totalSize) {
					break;
				}
				answer.push_back(matrix[top][i]);
			}
			for (int i = top + 1; i < bottom; i++) {
				if (answer.size() >= totalSize) {
					break;
				}
				answer.push_back(matrix[i][right-1]);
			}
			for (int i = right-2; i > left-1; i--) {
				if (answer.size() >= totalSize) {
					break;
				}
				answer.push_back(matrix[bottom - 1][i]);
			}
			for (int i = bottom-2; i > top; i--) {
				if (answer.size() >= totalSize) {
					break;
				}
				answer.push_back(matrix[i][left]);
			}
			left += 1;
			right -= 1;
			top += 1;
			bottom -= 1;
		}
		return answer;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
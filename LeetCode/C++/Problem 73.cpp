// LeetCode: Problem 73
// Jonathan Kosasih
/*
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
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
	void setZeroes(vector<vector<int>>& matrix) {
		if (matrix.empty()) {
			return;
		}
		int rows = matrix.size();
		int columns = matrix[0].size();
		bool firstRow = false;
		bool firstCol = false;
		for (int i = 0; i < columns; i++) {
			if (matrix[0][i] == 0) {
				firstRow = true;
			}
		}
		for (int i = 0; i < rows; i++) {
			if (matrix[i][0] == 0) {
				firstCol = true;
			}
		}

		for (int i = 1; i < rows; i++) {
			for (int j = 1; j < columns; j++) {
				if (matrix[i][j] == 0) {
					matrix[0][j] = matrix[i][0] = 0;
				}
			}
		}

		for (int i = 1; i < columns; i++) {
			if (matrix[0][i] == 0) {
				for (int j = 1; j < rows; j++) {
					matrix[j][i] = 0;
				}
			}
		}

		for (int i = 1; i < rows; i++) {
			if (matrix[i][0] == 0) {
				for (int j = 1; j < columns; j++) {
					matrix[i][j] = 0;
				}
			}
		}

		if (firstRow) {
			for (int i = 0; i < columns; i++) {
				matrix[0][i] = 0;
			}
		}
		if (firstCol) {
			for (int i = 0; i < rows; i++) {
				matrix[i][0] = 0;
			}
		}
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
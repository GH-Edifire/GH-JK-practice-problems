// LeetCode: Problem 48
// Jonathan Kosasih
/*
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

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
	void rotate(vector<vector<int>>& matrix) {
		int length = matrix.size();
		// transpose
		for (int i = 0; i < length; i++) {
			for (int j = 0; j < i; j++) {
				std::swap(matrix[i][j], matrix[j][i]);
			}
		}
		// reverse rows
		for (int i = 0; i < length; i++) {
			std::reverse(matrix[i].begin(), matrix[i].end());
		}
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
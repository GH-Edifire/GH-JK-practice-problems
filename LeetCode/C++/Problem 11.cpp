// LeetCode: Problem 11
// Jonathan Kosasih
/*
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
*/
//-------------------------------------------------------------------

#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <string>
#include <algorithm> 
using std::vector;
using std::map;
using std::unordered_map;
using std::set;

class Solution {
public:
	int maxArea(vector<int>& height) {
		int biggestArea = 0;
		int left = 0;
		int right = height.size()-1;
		while (left < right) {
			int area = std::min(height[left], height[right]) * (right - left);
			if (area > biggestArea) {
				biggestArea = area;
			}
			if (height[left] < height[right]) {
				left += 1;
			}
			else {
				right -= 1;
			}
		}
		return biggestArea;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
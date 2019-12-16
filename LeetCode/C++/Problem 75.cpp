// LeetCode: Problem 75
// Jonathan Kosasih
/*
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
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
	void sortColors(vector<int>& nums) {
		int left = 0;
		int mid = 0;
		int right = nums.size()-1;
		while (mid <= right) {
			if (nums[mid] == 0) {
				std::swap(nums[left], nums[mid]);
				left += 1;
				mid += 1;
			}
			else if (nums[mid] == 2) {
				std::swap(nums[mid], nums[right]);
				right -= 1;
			}
			else {
				mid += 1;
			}
		}
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
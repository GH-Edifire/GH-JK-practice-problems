// LeetCode: Problem 34
// Jonathan Kosasih
/*
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
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
	vector<int> searchRange(vector<int>& nums, int target) {
		int start = 0;
		int end = nums.size();
		int left, mid, right;
		// find start of target
		while (start < end) {
			mid = (start + end) / 2;
			if (nums[mid] >= target) {
				end = mid;
			}
			else {
				start = mid + 1;
			}
		}
		left = start;
		// find end of target, beginning index of another number
		start = 0;
		end = nums.size();
		while (start < end) {
			mid = (start + end) / 2;
			if (nums[mid] > target) {
				end = mid;
			}
			else {
				start = mid + 1;
			}
		}
		right = start;
		// left and right should be different values, right should at least be +1 to left
		return left == right ? vector<int> {-1, -1} : vector<int>{ left, right - 1 };
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
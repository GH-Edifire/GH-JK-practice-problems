// LeetCode: Problem 33
// Jonathan Kosasih
/*
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
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
	int search(vector<int>& nums, int target) {
		if (nums.empty()) {
			return -1;
		}
		int low = 0;
		int high = nums.size() - 1;
		while (low <= high) {
			int mid = (low + high) / 2;
			if (target == nums[mid]) {
				return mid;
			}
			if (nums[low] <= nums[mid]) {
				if (nums[low] <= target && target <= nums[mid]) {
					high = mid - 1;
				}
				else {
					low = mid + 1;
				}
			}
			else {
				if (nums[mid] <= target && target <= nums[high]) {
					low = mid + 1;
				}
				else {
					high = mid - 1;
				}
			}
		}
		return -1;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
// LeetCode: Problem 55
// Jonathan Kosasih
/*
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
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
	bool canJump(vector<int>& nums) {
		if (nums.empty()) {
			return false;
		}
		int totalSize = nums.size();
		int currentReach = nums[0];
		for (int i = 0; i < totalSize; i++) {
			if (currentReach < i) {
				return false;
			}
			if (currentReach >= totalSize - 1) {
				return true;
			}
			currentReach = std::max(currentReach, i + nums[i]);
		}
		return false;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
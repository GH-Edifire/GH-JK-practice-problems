// LeetCode: Problem 53
// Jonathan Kosasih
/*
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
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
	int maxSubArray(vector<int>& nums) {
		if (nums.empty()) {
			return 0;
		}
		int greatestSum = nums[0];
		int currentSum = nums[0];
		for (int i = 1; i < nums.size(); i++) {
			currentSum = std::max(nums[i], currentSum + nums[i]);
			greatestSum = std::max(greatestSum, currentSum);
		}
		return greatestSum;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
// LeetCode: Problem 1
// Jonathan Kosasih
/*
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/
//-------------------------------------------------------------------

#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
using std::vector;
using std::map;
using std::unordered_map;

class Solution {
public:
	vector<int> twoSum(vector<int>& nums, int target) {
		unordered_map<int,int> data;
		for (int i = 0; i < nums.size(); i++) {
			int comp = target - nums[i];
			if (data.find(comp) != data.end()) {
				return { data[comp], i };
			}
			data[nums[i]] = i;
		}
		return {};
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
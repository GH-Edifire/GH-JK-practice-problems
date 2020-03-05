// LeetCode: Problem 198
// Jonathan Kosasih
/*
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically 
contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
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
#include <queue>
#include <deque>
#include <numeric>
using std::vector;
using std::map;
using std::unordered_map;
using std::set;
using std::stack;
using std::queue;
using std::deque;
using std::accumulate;

class Solution {
public:
	int rob(vector<int>& nums) {
		if (nums.empty()) {
			return 0;
		}
		if (nums.size() <= 2) {
			return *std::max_element(nums.begin(), nums.end());
		}
		vector<int> ans;
		ans.push_back(nums[0]);
		// std::max_element(INCLUSIVE, EXCLUSIVE)
		ans.push_back(*std::max_element(nums.begin(), nums.begin() + 2));
		for (int i = 2; i < nums.size(); i++) {
			// track what's bigger: current + ans[i-2] or ans[i-1]
			ans.push_back(std::max((nums[i] + ans[i - 2]), ans[i - 1]));
		}
		return ans.back();
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
// LeetCode: Problem 152
// Jonathan Kosasih
/*
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
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
	int maxProduct(vector<int>& nums) {
		if (nums.size() == 0) {
			return 0;
		}
		int big = nums[0], small = nums[0], ans = nums[0];
		for (int i = 1; i < nums.size(); i++) {
			int temp = big;
			vector<int> compare = { temp * nums[i], nums[i], small * nums[i] };
			big = *max_element(compare.begin(), compare.end());
			small = *min_element(compare.begin(), compare.end());
			if (big > ans) {
				ans = big;
			}
		}
		return ans;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
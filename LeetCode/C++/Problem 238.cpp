// LeetCode: Problem 238
// Jonathan Kosasih
/*
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
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
	vector<int> productExceptSelf(vector<int>& nums) {
		int n = nums.size();
		int left = 1;
		int right = 1;
		vector<int> ans(n, 1);

		for (int i = 0; i < n; i++) {
			ans[i] *= left;
			left *= nums[i];
			ans[n - 1 - i] *= right;
			right *= nums[n - 1 - i];
		}
		return ans;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
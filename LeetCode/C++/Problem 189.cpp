// LeetCode: Problem 189
// Jonathan Kosasih
/*
Given an array, rotate the array to the right by k steps, where k is non-negative.
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
	// reverse 3 times
	void rotate(vector<int>& nums, int k) {
		k %= nums.size();
		reverse(nums.begin(), nums.end());
		reverse(nums.begin() + k, nums.end());
		reverse(nums.begin(), nums.begin() + k);
	}
	// use extra array
	void rotate2(vector<int>& nums, int k) {
		vector<int> temp(nums.size(), 0);
		for (int i = 0; i < nums.size(); i++) {
			temp[(i + k) % nums.size()] = nums[i];
		}
		for (int i = 0; i < nums.size(); i++) {
			nums[i] = temp[i];
		}
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
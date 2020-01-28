// LeetCode: Problem 136
// Jonathan Kosasih
/*
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
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
	int singleNumber(vector<int>& nums) {
		int ans = 0;
		for (int i = 0; i < nums.size(); i++) {
			ans ^= nums[i];
		}
		return ans;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
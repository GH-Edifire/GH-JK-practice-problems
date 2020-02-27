// LeetCode: Problem 179
// Jonathan Kosasih
/*
Given a list of non negative integers, arrange them such that they form the largest number.
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
	struct comp {
		bool operator() (int a, int b) {
			string comp1 = to_string(a) + to_string(b);
			string comp2 = to_string(b) + to_string(a);
			return comp1 > comp2;
		}
	} myComp;
public:
	string largestNumber(vector<int>& nums) {
		sort(nums.begin(), nums.end(), myComp);
		if (nums[0] == 0) return "0";
		string ans = "";
		for (auto num : nums) {
			ans = ans + to_string(num);
		}
		return ans;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
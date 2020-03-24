// LeetCode: Problem 217
// Jonathan Kosasih
/*
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
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
	// use set
	bool containsDuplicate(vector<int>& nums) {
		set<int> table;
		for (int num : nums) {
			if (table.find(num) != table.end()) {
				return true;
			}
			table.insert(num);
		}
		return false;
	}
	// sort then check
	bool containsDuplicate2(vector<int>& nums) {
		sort(nums.begin(), nums.end());
		for (int i = 1; i < nums.size(); i++)
			if (nums[i] == nums[i - 1]) return true;
		return false;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
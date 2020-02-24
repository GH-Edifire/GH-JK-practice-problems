// LeetCode: Problem 169
// Jonathan Kosasih
/*
Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times.

You may assume that the array is non-empty and the majority element always exist in the array.
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
	int majorityElement(vector<int>& nums) {
		unordered_map<int, int> counter;
		for (int num : nums) {
			if (++counter[num] > nums.size() / 2) {
				return num;
			}
		}
		return 0;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
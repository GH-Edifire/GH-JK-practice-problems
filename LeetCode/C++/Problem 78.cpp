// LeetCode: Problem 78
// Jonathan Kosasih
/*
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
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
	vector<vector<int>> subsets(vector<int>& nums) {
		vector<vector<int>> answer = { {} };
		std::sort(nums.begin(), nums.end());
		for (int num : nums) {
			int size = answer.size();
			for (int i = 0; i < size; i++) {
				answer.push_back(answer[i]);
				answer.back().push_back(num);
			}
		}
		return answer;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
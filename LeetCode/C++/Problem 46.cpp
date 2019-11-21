// LeetCode: Problem 46
// Jonathan Kosasih
/*
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

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

class Solution{
public:
	vector<vector<int> > permute(vector<int> & num) {
		vector<vector<int> > result;

		permuteRecursive(num, 0, result);
		return result;
	}

	// permute num[begin..end]
	// invariant: num[0..begin-1] have been fixed/permuted
	void permuteRecursive(vector<int> & num, int begin, vector<vector<int> > & result) {
		if (begin >= num.size()) {
			// one permutation instance
			result.push_back(num);
			return;
		}

		for (int i = begin; i < num.size(); i++) {
			swap(num[begin], num[i]);
			permuteRecursive(num, begin + 1, result);
			// reset
			swap(num[begin], num[i]);
		}
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
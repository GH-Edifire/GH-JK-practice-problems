// LeetCode: Problem 22
// Jonathan Kosasih
/*
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
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

class Solution {
public:
	vector<string> generateParenthesis(int n) {
		vector<string> ans;
		addingPar(ans, "", n, 0);
		return ans;
	}
	void addingPar(vector<string>& v, string str, int l , int r) {
		if (l == 0 && r == 0) {
			v.push_back(str);
			return;
		}
		if (r > 0) { addingPar(v, str + ")", l, r - 1); }
		if (l > 0) { addingPar(v, str + "(", l - 1, r + 1); }
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
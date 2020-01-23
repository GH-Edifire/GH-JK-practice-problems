// LeetCode: Problem 131
// Jonathan Kosasih
/*
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.
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
using std::vector;
using std::map;
using std::unordered_map;
using std::set;
using std::stack;
using std::queue;
using std::deque;

class Solution {
public:
	vector<vector<string>> partition(string s) {
		vector<vector<string>> pars;
		vector<string> par;
		partition(s, 0, par, pars);
		return pars;
	}
private:
	void partition(string& s, int start, vector<string>& par, vector<vector<string>>& pars) {
		int n = s.length();
		if (start == n) {
			pars.push_back(par);
		}
		else {
			for (int i = start; i < n; i++) {
				if (isPalindrome(s, start, i)) {
					par.push_back(s.substr(start, i - start + 1));
					partition(s, i + 1, par, pars);
					par.pop_back();
				}
			}
		}
	}

	bool isPalindrome(string& s, int l, int r) {
		while (l < r) {
			if (s[l++] != s[r--]) {
				return false;
			}
		}
		return true;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
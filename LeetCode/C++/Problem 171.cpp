// LeetCode: Problem 171
// Jonathan Kosasih
/*
Given a column title as appear in an Excel sheet, return its corresponding column number.
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
	int titleToNumber(string s) {
		int ans = 0;
		for (int i = 0; i < s.length(); i++) {
			ans *= 26;
			ans += s[i] - 'A' + 1;
		}
		return ans;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
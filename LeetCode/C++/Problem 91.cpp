// LeetCode: Problem 91
// Jonathan Kosasih
/*
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.
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
	int numDecodings(string s) {
		if (s.empty()) return 0;
		if (s.size() == 1 && stoi(s) != 0) return 1;
		int dn_minus_2 = s[0] != '0' ? 1 : 0; // [1:9] are valid one-digit encoding
		int dn_minus_1 = s[1] != '0' ? dn_minus_2 : 0;
		int dn = 0;
		for (int i = 2; i <= s.size(); ++i) {
			int one = stoi(s.substr(i - 1, 1)), two = stoi(s.substr(i - 2, 2));
			dn = (one != 0) ? dn_minus_1 : 0;
			dn += (10 <= two && two <= 26) ? dn_minus_2 : 0; // [10:26] are valid two-digit encoding
			dn_minus_2 = dn_minus_1;
			dn_minus_1 = dn;
		}
		return dn;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
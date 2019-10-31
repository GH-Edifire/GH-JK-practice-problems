// LeetCode: Problem 5
// Jonathan Kosasih
/*
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
*/
//-------------------------------------------------------------------

#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
using std::vector;
using std::map;
using std::unordered_map;
using std::set;

class Solution {
public:
	string longestPalindrome(string s) {
		if (s.empty()) {
			return "";
		}
		string ans = "";
		int maxLen = 0;
		int inputLength = s.size();
		bool dp[inputLength][inputLength] = { {false} };
		// initialize 1 letter palindromes
		for (int i = 0; i < inputLength; i++) {
			dp[i][i] = true;
		}
		maxLen = 1;
		ans = s[0];
		// initialize 2 letter palindromes
		for (int i = 0; i < inputLength-1 ; i++) {
			if (s[i] == s[i + 1]) {
				dp[i][i + 1] = true;
				ans = s.substr(i, 2);
				maxLen = 2;
			}
		}
		// fill in the rest with DP
		// go by column first
		// check with dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
		for (int j = 2; j < inputLength; j++) {
			for (int i = 0; i < j; i++) {
				if (s[i] == s[j] && dp[i + 1][j - 1]) {
					dp[i][j] = true;
					if (maxLen < (j - i + 1)) {
						maxLen = j - i + 1;
						ans = s.substr(i, maxLen);
					}
				}
			}
		}
		return ans;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
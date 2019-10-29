// LeetCode: Problem 3
// Jonathan Kosasih
/*
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
			 Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
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
	int lengthOfLongestSubstring(string s) {
		int start = 0;
		int maxLength = 0;
		unordered_map<char,int> usedChars;
		for (int i = 0; i < s.size(); i++) {
			if (usedChars.count(s[i]) && start <= usedChars[s[i]]) {
				start = usedChars[s[i]] + 1;
			}
			else {
				maxLength = max(maxLength, i - start + 1);
			}
			usedChars[s[i]] = i;
		}
		return maxLength;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
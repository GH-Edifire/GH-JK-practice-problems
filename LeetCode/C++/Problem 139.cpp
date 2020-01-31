// LeetCode: Problem 139
// Jonathan Kosasih
/*
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
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
	bool wordBreak(string s, vector<string>& wordDict) {
		if (wordDict.size() == 0) {
			return false;
		}
		int stringLength = s.size();
		vector<bool> memo(stringLength + 1, false);
		memo[0] = true;

		for (int i = 0; i < stringLength; i++) {
			for (string& word : wordDict) {
				int wordLength = word.length();
				if (i+1-wordLength >= 0 && s.substr(i+1-wordLength,wordLength) == word && memo[i+1-wordLength]) {
					memo[i + 1] = true;
					break;
				}
			}
		}
		return memo.back();
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
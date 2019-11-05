// LeetCode: Problem 14
// Jonathan Kosasih
/*
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
*/
//-------------------------------------------------------------------

#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <string>
#include <algorithm> 
using std::vector;
using std::map;
using std::unordered_map;
using std::set;

class Solution {
public:
	string longestCommonPrefix(vector<string>& strs) {
		int n = strs.size();
		if (n == 0) {
			return "";
		}
		string res = "";
		sort(strs.begin(), strs.end()); // sort the array by alphabetical-increasing order, not length
		string first = strs[0]; // first word
		string last = strs[n - 1]; // last word
		int limit = min(first.length(), last.length());
		for (int i = 0; i < limit; i++) { // find out the longest common prefix between first and last word
			if (first[i] == last[i]) {
				res += first[i];
			}
			else {
				break;
			}
		}
		return res;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
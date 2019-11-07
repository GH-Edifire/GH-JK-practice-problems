// LeetCode: Problem 17
// Jonathan Kosasih
/*
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
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
	vector<string> letterCombinations(string digits) {
		vector<string> ans;
		unordered_map<char, string> buttons = { {'2', "abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"}, {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"} };
		for (int i = 0; i < digits.size(); i++) {
			if (ans.size() == 0) {
				for (int j = 0; j < buttons[digits[i]].size(); j++) {
					ans.push_back(buttons[digits[i]].substr(j, 1));
				}
			}
			else {
				vector<string> placeholder;
				for (int j = 0; j < ans.size(); j++) {
					for (int k = 0; k < buttons[digits[i]].size(); k++) {
						placeholder.push_back(ans[j] + buttons[digits[i]].substr(k, 1));
					}
				}
				ans = placeholder;
			}
		}
		return ans;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
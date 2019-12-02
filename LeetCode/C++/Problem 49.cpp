// LeetCode: Problem 49
// Jonathan Kosasih
/*
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
All inputs will be in lowercase.
The order of your output does not matter.
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
	vector<vector<string>> groupAnagrams(vector<string>& strs) {
		unordered_map<string, vector<string>> sortingDictionary;
		for (string str : strs) {
			string word = str;
			std::sort(word.begin(), word.end());
			sortingDictionary[word].push_back(str);
		}

		vector<vector<string>> answer;
		for (auto entry : sortingDictionary) {
			answer.push_back(entry.second);
		}
		return answer;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
// LeetCode: Problem 125
// Jonathan Kosasih
/*
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
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
	// two pointers, compare only alphanumeric
	bool isPalindrome(string s) {
		for (int i = 0, j = s.size() - 1; i < j; i++, j--) {
			while (isalnum(s[i]) == false && i < j) i++; // move left pointer until we find alphanum
			while (isalnum(s[j]) == false && i < j) j--; // move right pointer until we find alphanum
			if (toupper(s[i]) != toupper(s[j])) return false; // compared chars dont match, retunr false
		}
		return true;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
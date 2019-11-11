// LeetCode: Problem 20
// Jonathan Kosasih
/*
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
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
	bool isValid(string s) {
		std::stack<char> stack;
		for (char& c : s) {
			switch (c) {
				case '(':
				case '[':
				case '{': {
					stack.push(c);
					break;
				}
				case ')': {
					if (stack.empty() || stack.top() != '(') {
						return false;
					}
					else {
						stack.pop();
						break;
					}
				}
				case ']': {
					if (stack.empty() || stack.top() != '[') {
						return false;
					}
					else {
						stack.pop();
						break;
					}
				}
				case '}': {
					if (stack.empty() || stack.top() != '{') {
						return false;
					}
					else {
						stack.pop();
						break;
					}
				}
				default: ;
			}
		}
		return stack.empty();
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
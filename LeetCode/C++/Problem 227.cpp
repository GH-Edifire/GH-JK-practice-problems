// LeetCode: Problem 227
// Jonathan Kosasih
/*
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
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
	int calculate(string s) {
		stack<int> myStack;
		char sign = '+';
		int res = 0;
		long int tmp = 0;
		for (unsigned int i = 0; i < s.size(); i++) {
			if (isdigit(s[i]))
				tmp = 10 * tmp + s[i] - '0';
			if (!isdigit(s[i]) && !isspace(s[i]) || i == s.size() - 1) {
				if (sign == '-')
					myStack.push(-tmp);
				else if (sign == '+')
					myStack.push(tmp);
				else {
					int num;
					if (sign == '*')
						num = myStack.top() * tmp;
					else
						num = myStack.top() / tmp;
					myStack.pop();
					myStack.push(num);
				}
				sign = s[i];
				tmp = 0;
			}
		}
		while (!myStack.empty()) {
			res += myStack.top();
			myStack.pop();
		}
		return res;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
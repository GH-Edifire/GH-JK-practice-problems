// LeetCode: Problem 150
// Jonathan Kosasih
/*
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
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
	int evalRPN(vector<string>& tokens) {
		if (tokens.empty()) {
			return 0;
		}
		stack<int> st;
		for (string s : tokens) {
			if (s == "+") {
				int tempOne = st.top();
				st.pop();
				int tempTwo = st.top();
				st.pop();
				st.push(tempTwo + tempOne);
			}
			else if (s == "-") {
				int tempOne = st.top();
				st.pop();
				int tempTwo = st.top();
				st.pop();
				st.push(tempTwo - tempOne);
			}
			else if (s == "/") {
				int tempOne = st.top();
				st.pop();
				int tempTwo = st.top();
				st.pop();
				st.push(tempTwo / tempOne);
			}
			else if (s == "*") {
				int tempOne = st.top();
				st.pop();
				int tempTwo = st.top();
				st.pop();
				st.push(tempTwo * tempOne);
			}
			else {
				st.push(std::stoi(s));
			}
		}
		return st.top();
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
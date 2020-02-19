// LeetCode: Problem 155
// Jonathan Kosasih
/*
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
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

class MinStack {
public:
	/** initialize your data structure here. */
	//MinStack() {
		//stack<pair<int, int>> minStack;
	//}

	stack<pair<int, int>> minStack;

	void push(int x) {
		int min;
		if (minStack.empty()) {
			min = x;
		}
		else {
			min = std::min(minStack.top().second, x);
		}
		minStack.push({ x, min });
	}

	void pop() {
		minStack.pop();
	}

	int top() {
		return minStack.top().first;
	}

	int getMin() {
		return minStack.top().second;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
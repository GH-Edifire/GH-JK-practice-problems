// LeetCode: Problem 70
// Jonathan Kosasih
/*
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
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
	int climbStairs(int n) {
		vector<int> answer;
		answer.push_back(1);
		answer.push_back(2);
		if (n <= 2) {
			return answer[n - 1];
		}
		for (int i = 2; i < n; i++) {
			int sumWays = answer[i - 2] + answer[i - 1];
			answer.push_back(sumWays);
		}
		return answer[answer.size() - 1];
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
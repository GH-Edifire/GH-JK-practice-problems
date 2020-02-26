// LeetCode: Problem 172
// Jonathan Kosasih
/*
Given an integer n, return the number of trailing zeroes in n!.
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

// Count the number of 5's, probably too many 2's to count
class Solution {
public:
	int trailingZeroes(int n) {
		int ans = 0;
		// 1st loop counts multiples of 5
		// 2nd loop counts multiples of 25
		// 3rd+ continues the pattern
		while (n) {
			n /= 5;
			ans += n;
		}
		return ans;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
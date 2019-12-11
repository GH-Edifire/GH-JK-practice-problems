// LeetCode: Problem 69
// Jonathan Kosasih
/*
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
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
	// integer square root, newton's method
	int mySqrt(int x) {
		long ans = x;
		while (ans * ans > x) {
			ans = (ans + x / ans) / 2;
		}
		return ans;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
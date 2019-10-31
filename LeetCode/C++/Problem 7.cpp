// LeetCode: Problem 7
// Jonathan Kosasih
/*
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
*/
//-------------------------------------------------------------------

#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <string>
using std::vector;
using std::map;
using std::unordered_map;
using std::set;

class Solution {
public:
	int reverse(int x) {
		int ans = 0;
		while (x) {
			// overflow check
			if (ans > INT_MAX / 10 || ans < INT_MIN / 10) {
				return 0;
			}
			int temp = ans * 10 + x % 10;
			// overflow check
			if (temp / 10 != ans)
				return 0;
			ans = temp;
			x /= 10;
		}
		return ans;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
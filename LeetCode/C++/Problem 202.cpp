// LeetCode: Problem 202
// Jonathan Kosasih
/*
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 
(where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.
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
	bool isHappy(int n) {
		int sum = 0, num = 0;
		set<int> s;
		s.insert(n);
		while (true)
		{
			sum = 0;
			// compute sum of digits
			while (n > 0)
			{
				num = n % 10;
				sum += num * num;
				n /= 10;
			}
			if (sum == 1) {
				return true;
			}
			else {
				n = sum;
			}
			// found number we already reached, infinite loop, terminate function
			if (s.find(n) != s.end()) {
				return false;
			}
			else {
				s.insert(n);
			}
		}
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
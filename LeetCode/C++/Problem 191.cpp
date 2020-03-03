// LeetCode: Problem 191
// Jonathan Kosasih
/*
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).
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
	int hammingWeight(uint32_t n) {
		int ans = 0;
		uint32_t temp = 0;
		for (int i = 0; i < 32; i++) {
			temp = ((n >> i) & 1);
			if (temp) {
				ans++;
			}
		}
		return ans;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
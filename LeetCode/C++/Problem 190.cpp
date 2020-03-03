// LeetCode: Problem 190
// Jonathan Kosasih
/*
Reverse bits of a given 32 bits unsigned integer.
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
	uint32_t reverseBits(uint32_t n) {
		int i = 0, j = 31;
		while (i < j) {
			if (((n >> i) & 1) != ((n >> j) & 1)) {
				n ^= ((1U << i) | (1U << j));
			}
			i++, j--;
		}
		return n;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
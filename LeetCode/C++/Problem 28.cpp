// LeetCode: Problem 28
// Jonathan Kosasih
/*
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
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
	// basically sliding window method
	int strStr(string haystack, string needle) {
		int m = haystack.size(), n = needle.size(), p = 0;
		while (p + n - 1 < m) {
			if (haystack.substr(p, n) == needle) {
				return p;
			}
			// if the first char isn't the same as the start of needle, skip it
			while (p++ + n - 1 < m && haystack[p] != needle[0]);
		}
		return -1;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
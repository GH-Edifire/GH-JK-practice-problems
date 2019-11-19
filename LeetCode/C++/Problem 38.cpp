// LeetCode: Problem 38
// Jonathan Kosasih
/*
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 <= n <= 30, generate the nth term of the count-and-say sequence.
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
	string countAndSay(int n) {
		if (n == 0) {
			return "";
		}
		string ans = "1";
		while (--n) {
			string cur = "";
			for (int i = 0; i < ans.size(); i++) {
				int count = 1;
				while ((i + 1 < ans.size()) && (ans[i] == ans[i + 1])) {
					count++;
					i++;
				}
				cur += to_string(count) + ans[i];
			}
			ans = cur;
		}
		return ans;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}
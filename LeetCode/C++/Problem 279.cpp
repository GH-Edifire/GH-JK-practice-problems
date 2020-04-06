// LeetCode: Problem 279
// Jonathan Kosasih
/*
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
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
    int numSquares(int n) {
        if (n == 0) return 0;

        vector<int> dp(n + 1, 0);

        for (int i = 0; i <= n; ++i) {
            dp[i] = i;
            for (int j = 2; j <= sqrt(i); ++j) {
                dp[i] = min(dp[i], 1 + dp[i - j * j]);
            }
        }

        return dp[n];
    }
};
int main()
{
    //std::cout << "Hello World!\n";
}
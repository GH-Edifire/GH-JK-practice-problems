// LeetCode: Problem 121
// Jonathan Kosasih
/*
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
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
using std::vector;
using std::map;
using std::unordered_map;
using std::set;
using std::stack;
using std::queue;
using std::deque;

class Solution {
public:
	int maxProfit(vector<int>& prices) {
		if (prices.empty()) {
			return 0;
		}
		int lowest = prices[0];
		int profit = 0;
		for (int i = 1; i < prices.size(); i++) {
			if (lowest > prices[i]) {
				lowest = prices[i];
			}
			else {
				if ((prices[i] - lowest) > profit) {
					profit = std::max(profit, prices[i] - lowest);
				}
			}
		}
		return profit;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
// LeetCode: Problem 134
// Jonathan Kosasih
/*
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
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
	int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
		if (gas.empty() || cost.empty() || (accumulate(gas.begin(), gas.end(), 0)) < accumulate(cost.begin(), cost.end(), 0)) {
			return -1;
		}
		int length = gas.size();
		int start = 0;
		int currentGas = 0;
		for (int i = 0; i < length; i++) {
			currentGas += gas[i] - cost[i];
			if (currentGas < 0) {
				currentGas = 0;
				start = i + 1;
			}
		}
		return start;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
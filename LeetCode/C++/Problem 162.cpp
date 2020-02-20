// LeetCode: Problem 162
// Jonathan Kosasih
/*
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ÅÇ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -Åá.
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
	int findPeakElement(const vector<int>& num) {
		int low = 0, high = num.size() - 1;
		while (low < high - 1) {
			int mid = (low + high) / 2;
			if (num[mid] > num[mid - 1] && num[mid] > num[mid + 1])
				return mid;
			else if (num[mid] > num[mid + 1])
				high = mid - 1;
			else
				low = mid + 1;
		}
		return num[low] > num[high] ? low : high;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
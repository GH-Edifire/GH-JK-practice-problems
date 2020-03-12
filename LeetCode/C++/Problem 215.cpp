// LeetCode: Problem 215
// Jonathan Kosasih
/*
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
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

// use max heap, largest number at top, pop k-1 times to find Kth largest
class Solution {
public:
	int findKthLargest(vector<int>& nums, int k) {
		priority_queue<int> pq(nums.begin(), nums.end());
		for (int i = 0; i < k - 1; i++) {
			pq.pop();
		}
		return pq.top();
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}
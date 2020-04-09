// LeetCode: Problem 287
// Jonathan Kosasih
/*
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
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
    // http://keithschwarz.com/interesting/code/find-duplicate/FindDuplicate.python.html
    // very difficult when thinking about the contraints for the first time
    // initially thought about using sorting, hashtable, or set but those dont fit the contraints
    int findDuplicate(vector<int>& nums) {
        int slow = 0, fast = 0, finder = 0;

        while (1)
        {
            slow = nums[slow];
            fast = nums[nums[fast]];

            if (slow == fast)
                break;
        }


        while (1)
        {
            finder = nums[finder];
            slow = nums[slow];

            if (finder == slow)
                return finder;
        }
    }
};
int main()
{
    //std::cout << "Hello World!\n";
}
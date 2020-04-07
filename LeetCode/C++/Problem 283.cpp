// LeetCode: Problem 283
// Jonathan Kosasih
/*
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
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
    void moveZeroes(vector<int>& nums) {
        int lastNumber = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                nums[lastNumber] = nums[i];
                lastNumber += 1;
            }
        }
        for (int i = lastNumber; i < nums.size(); i++) {
            nums[i] = 0;
        }
    }
};
int main()
{
    //std::cout << "Hello World!\n";
}